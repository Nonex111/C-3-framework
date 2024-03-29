import os
from easydict import EasyDict as edict
import time
import torch

# init
__C = edict()
cfg = __C

__C.PLATFORM = 'kaggle'

# EXP_PATH: the path of logs, checkpoints, and current codes
if __C.PLATFORM == 'local':
	__C.EXP_PATH = './exp'
elif __C.PLATFORM == 'colab':
	__C.EXP_PATH = '/content/drive/My Drive/Checkpoint/C^3 Framework/exp'
elif __C.PLATFORM == 'kaggle':
	__C.EXP_PATH = '/kaggle/working/Checkpoint/C^3Framework/exp'

#------------------------------TRAIN------------------------
__C.SEED = 3035 # random seed,  for reproduction		# 3407 is all you need?
__C.DATASET = 'SHHB' # dataset selection: GCC, SHHA, SHHB, UCF50, QNRF, WE, Mall, UCSD

if __C.DATASET == 'UCF50':# only for UCF50
	from datasets.UCF50.setting import cfg_data
	__C.VAL_INDEX = cfg_data.VAL_INDEX 

if __C.DATASET == 'GCC':# only for GCC
	from datasets.GCC.setting import cfg_data
	__C.VAL_MODE = cfg_data.VAL_MODE 


__C.NET = 'CSRNet' # net selection: MCNN, AlexNet, VGG, VGG_DECODER, Res50, CSRNet, SANet,Res101_SFCN

__C.PRE_GCC = False # use the pretrained model on GCC dataset
__C.PRE_GCC_MODEL = 'path to model' # path to model

__C.RESUME = False # contine training
__C.RESUME_PATH = os.path.join(__C.EXP_PATH, '12-18_22-02_SHHB_VGG_1e-05/latest_state.pth')

__C.GPU_ID = [0] # sigle gpu: [0], [1] ...; multi gpus: [0,1]

# learning rate settings
__C.LR = 1e-5 # learning rate
__C.LR_DECAY = 0.995 # decay rate
__C.LR_DECAY_START = -1 # when training epoch is more than it, the learning rate will be begin to decay
__C.NUM_EPOCH_LR_DECAY = 1 # decay frequency
__C.MAX_EPOCH = 200

# multi-task learning weights, no use for single model, such as MCNN, VGG, VGG_DECODER, Res50, CSRNet, and so on

__C.LAMBDA_1 = 1e-4# SANet:0.001 CMTL 0.0001


# print 
__C.PRINT_FREQ = 10

now = time.strftime("%m-%d_%H-%M", time.localtime())

__C.EXP_NAME = now \
			 + '_' + __C.DATASET \
             + '_' + __C.NET \
             + '_' + str(__C.LR)

if __C.DATASET == 'UCF50':
	__C.EXP_NAME += '_' + str(__C.VAL_INDEX)	

if __C.DATASET == 'GCC':
	__C.EXP_NAME += '_' + __C.VAL_MODE





#------------------------------VAL------------------------
__C.VAL_DENSE_START = 50
__C.VAL_FREQ = 10 # Before __C.VAL_DENSE_START epoches, the freq is set as __C.VAL_FREQ

#------------------------------VIS------------------------
__C.VISIBLE_NUM_IMGS = 1 #  must be 1 for training images with the different sizes



#================================================================================
#================================================================================
#================================================================================  
