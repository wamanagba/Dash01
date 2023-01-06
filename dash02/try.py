import xarray as xr
import pandas as pd
import os

data_folder = '/Users/yacoub/Desktop/Training/Data/dash02_climate'
output_folder = 'output'

def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

filename = 'gistemp1200_GHCNv4_ERSSTv5.nc'
data_url = 'https://github.com/spatialthoughts/python-dataviz-web/raw/main/data/gistemp/'

download(data_url + filename)

netcdf_dir = '/Users/yacoub/Desktop/Training/Data/dash02_climate/'

csv_dir = netcdf_dir + '/csv/'

netcdf_file_name = 'gistemp1200_GHCNv4_ERSSTv5.nc'

netcdf_file_in = netcdf_dir + netcdf_file_name
print(netcdf_file_in)
csv_file_out = csv_dir + netcdf_file_name[:-3] + '.csv'
print(csv_file_out)