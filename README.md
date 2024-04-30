# ex_netcdf

Ejemplos de netCDF en python

## Se requiere:
- netCDF4
```
conda install -c conda-forge netCDF4
```
- cartopy
```
conda install conda-forge::cartopy
```
  - documentación: [https://scitools.org.uk/cartopy/docs/latest/](https://scitools.org.uk/cartopy/docs/latest/)

## read_data_nc.py

Abre un archivo netCDF en modo de lectura para obtener información básica de su contenido.

### Ejecución
```
python read_data_nc.py archivo.nc
```

- read_data_nc.py nombre del script
- archivo.nc nombre del archivo netCDF que deseamos abrir


### plot_data_nc.py

Realiza la gráfica de la variable T2, en el tiempo 12, convirtiendo de K a C (línea 13).
Toma como referencia de latitud y longitud las variables _XLAT_ y _XLONG_ en el tiempo 0, la latitud y longitud no cambian en el tiempo, por lo que se puede tomar en cualquier tiempo (líneas 14 y 15)

### plot_data_shp_nc.py

Realiza la gráfica de la variable T2 de manera similar a plot_data_nc.py pero ahora agrega información extraida de un shapefile 
