import json
import pickle
import numpy as np

__genre = None
__data_columns = None
__model = None

'''def def get_context_data(genre, **kwargs):
    context = super(ViewName, self).get_context_data(**kwargs)
    return context'''

def get_estimated_Imdb():
    return __genre

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_colums
    global __genre

    with open("./artifacts/columns.json",'r') as f:
        __data_columns =  json.load(f)['data_columns']
        __genre = __data_columns[2:]

    with open("./artifacts/.pickle",'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")

if __name__  == "__main__":
    print(get_genre_names())
    