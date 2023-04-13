from netCDF4 import Dataset
from matplotlib import pyplot as plt
import cartopy.crs as ccrs


from sys import argv

filename = argv[1]
print(filename)
root=Dataset(filename, 'r')

#lee datos
#T2 = root.variables['T2'][12]-273.15
T2 = root.variables['RAINC'][12]+ root.variables['RAINNC'][12]
lat = root.variables['lat'][:]
lon = root.variables['lon'][:]

#obtiene limites
latmin = lat[0, 0]
latmax = lat[-1, 0]
lonmin = lon[0, 0]
lonmax = lon[0, -1]

proj = ccrs.PlateCarree()
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

plt.savefig('figure_nc.png')
