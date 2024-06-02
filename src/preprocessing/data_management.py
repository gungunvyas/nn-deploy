import os 
import pandas as pd
import pickle

from src.config import config

def load_dataset(file_name):

    file_path = os.path.join(config.datapath,file_name) #output --> "/src/datsets/file_name" ex file_name = train.csv

    data = pd.read_csv(file_path)

    return data 

def save_model(theta0,theta):

    pkl_file_path = os.path.join(config.saved_model_path,"two_input_xor_nn.pkl")

    with open(pkl_file_path,"wb") as file_handle:

        file_handle.dump({"params": {"biases":theta0,"weights":theta},"activations":config.f})

def load_model(file_name):
    pkl_file_path = os.path.join(config.saved_model_path,file_name)

    with open(pkl_file_path,"rb") as file_handle:

        loaded_model = file_handle.load()

    return loaded_model
