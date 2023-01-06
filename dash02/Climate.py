import xarray as xr
import pandas as pd
import os


Month="Aug"
Month_name="August"
Year='2022'


data_folder = '/Users/yacoub/Desktop/Training/Data/dash02_climate'
output_folder = 'output'

if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)



def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

filename = 'data.nc'
data_url = "https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.CPC/.CAMS_OPI/.v0208/.mean/.prcp/T/" \
           "("+Month+"%20"+Year+")/("+Month+"%20"+Year+")/RANGEEDGES/Y/-40/0.5/40/GRID/X/-25/0.5/55/GRID/" \
                                                       "%5BT%5D/average/31/mul/"

download(data_url + filename)

netcdf_dir = '/Users/yacoub/Desktop/Training/Data/dash02_climate/'

csv_dir = netcdf_dir + 'csv/'
netcdf_file_name = 'data.nc'

netcdf_file_in = netcdf_dir + netcdf_file_name
print(netcdf_file_in)
csv_file_out = csv_dir + netcdf_file_name[:-3] + '.csv'
print(csv_file_out)

ds = xr.open_dataset(netcdf_file_in)
df = ds.to_dataframe()
df.to_csv(csv_file_out)

ds





