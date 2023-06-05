import numpy as np
#import xarray as x
from datetime import datetime
#import pickle
import pandas as pd
#import code
#code.interact(local=dict(globals(), **locals()))

for i in [2,3,4,5,6,7,8,9,10]:
    CL=f'CL{i}'

    #The data of cyclones are : each line for each point of cyclone occurence,
    #column 0 number of id of cyclone, 1 lon, 2 lat, 3 year, 4 month, 5 day, 6 hour, 7 intensity?
    filename = f'/home/yseut/MetMed_work/data/storm_types/cyclones/TRACKS_{CL}.dat'
    with open(filename, 'r') as f:
        table = f.read()
    rows = table.count('\n')
    matrix = np.fromstring(table, sep=' ').reshape(rows, 8)

# Create panda Dataframe
    index = list(range(len(matrix)))
    df_cyclones = pd.DataFrame(matrix, index = index, columns = ['id_cyclone', 'lon', 'lat', 'year', 'month', 'day', 'hour', 'intensity'])
    df_cyclones['datetime'] = pd.to_datetime(df_cyclones[['year','month','day','hour']])

# Keep only cyclones in subdomain
    lonmin, latmin = -5, 36
    lonmax, latmax = 15, 45
    df_cyclones_dmn = df_cyclones[((df_cyclones['lon']>lonmin) & (df_cyclones['lon']<lonmax)) & ((df_cyclones['lat']>latmin) & (df_cyclones['lat']<latmax))] 
