
# coding: utf-8

# In[3]:

from pandas import HDFStore
import pandas as pd
import h5py


# In[46]:

def hdf5_to_csv(filename): 
    
      """
    Converts hdf5 files to csv

    Parameters
    ----------
    filename: string or list of strings
        Name of the hdf5 file being converted

    Returns
    -------
    Rewrites hdf5 keys to invidual csv files (returns nothing)
    """
        
    store = HDFStore(filename)
    for key in range(len(store.keys())):
        store[store.keys()[key]].to_csv(store.keys()[key][1:] + '.csv')


# In[39]:

# hdf5 files can also be dumped into an asci file with the following line in the command prompt

h5dump -o dset.asci -y -w 400 sanfran_public.h5

