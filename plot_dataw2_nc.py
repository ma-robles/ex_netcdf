from netCDF4 import Dataset
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.vector_transform as cvt



from sys import argv

filename = argv[1]
print(filename)
root=Dataset(filename, 'r')

#define proyeccion
proj = ccrs.PlateCarree()
#lee datos
T2 = root.variables['T2'][12]
lat = root.variables['lat'][:]
lon = root.variables['lon'][:]
u = root.variables['U10'][:][12]
v = root.variables['V10'][:][12]

#obtiene limites
latmin = lat[0, 0]
latmax = lat[-1, 0]
lonmin = lon[0, 0]
lonmax = lon[0, -1]

plt.figure()
ax_lim= [lonmin, lonmax, latmin, latmax]
ax = plt.axes(projection= proj)
ax.set_extent(ax_lim, proj)
#dibuja grid
ax.gridlines(draw_labels=["top", "right"], dms=True, x_inline=False, y_inline=False)
#dibuja lineas de costa
ax.coastlines()
# graficacion de variable
var_map = plt.contourf(lon, lat, T2, transform= proj )
#color bar
cbar=plt.colorbar(
        var_map,
        #ax=ax,
        #shrink=0.75,
        orientation='horizontal',
        aspect=50,
        pad=0.02,
        fraction=0.03,
        )
cbar.ax.set_xlabel('Variable')
wplot=ax.streamplot(
        lon,
        lat,
        u,v,
        #linewidth=1,
        #density=2,
        color='red',
        #cmap=plt.cm.tab10,
        #levels=np.arange(0,2,0.2),
        zorder=5,
        )

plt.savefig('figure_nc.png')
