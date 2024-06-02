import os
import pathlib
import src

NUM_INPUTS = 2
NUM_LAYERS = 3
P = [NUM_INPUTS,2,1]


f = [None,"Linear","Sigmoid"]

loss_function="mean squared error"
mini_batch_size=1

package_root = pathlib.Path(src.__file__).resolve().parent

datapath = os.path.join(package_root,"datasets") #output --> "/src/datasets"

saved_model_path = os.path.join(package_root,"trained_models") #output --> "/src/trained_models"

#theta0 = [None]
#theta = [None]

#z = [None]*NUM_LAYERS
#h = [None]*NUM_LAYERS


'''del_fl_by_del_z = [None]*NUM_LAYERS
del_hl_by_del_theta0 = [None]*NUM_LAYERS
del_hl_by_del_theta = [None]*NUM_LAYERS
del_L_by_del_h = [None]*NUM_LAYERS
del_L_by_del_theta0 = [None]*NUM_LAYERS
del_L_by_del_theta = [None]*NUM_LAYERS'''