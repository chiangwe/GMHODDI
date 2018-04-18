##############################################
#Package needed
##############################################

from numpy  import array
import cPickle as pickle
from copy import deepcopy
from scipy.sparse import *
import numpy as np
from scipy import sparse
import cPickle
import random
import pdb
import scipy.io as sio
import math
import shelve
from collections import Counter
import itertools
import multiprocessing
import sys
from scipy.optimize import linear_sum_assignment
import math
import time
from parse import csr_parse

##############################################
#Parameter for Calculate SDS based on Comedication
##############################################

print "======================================"
print "Graph Matching"
print "python SDS_CoMed.py ./CoMed_Feature_Plus_path ./CoMed_Feature_Minus_path ./Output_path"
print "======================================"


para = []
for arg in sys.argv:
        print arg
        para.append(arg)

C_Plus_path = para[1]
C_Minus_path = para[2]
OutputPath = para[3]

if len(para) != 4 : 
	exit()

##############################################
#reading Input
##############################################

Myo_sim = np.asmatrix( np.loadtxt(C_Plus_path) );
NonMyo_sim = np.asmatrix( np.loadtxt(C_Minus_path) );

##############################################
#Calculate similarity based on Drug Comedication
##############################################

Myo_sim_sum = array(Myo_sim.sum(0))[0]
index_zeros = np.where( Myo_sim_sum==0)
Myo_sim_sum[index_zeros] = 1
Myo_sim_sum = np.divide(1,Myo_sim_sum)
Myo_sim_sum[index_zeros] = 0
Myo_sim_sum = np.repeat(np.matrix(Myo_sim_sum,),Myo_sim.shape[0], axis=0)
Myo_sim_out = np.multiply( Myo_sim,Myo_sim_sum)

NonMyo_sim_sum = array(NonMyo_sim.sum(0))[0]
index_zeros = np.where( NonMyo_sim_sum==0)
NonMyo_sim_sum[index_zeros] = 1
NonMyo_sim_sum = np.divide(1,NonMyo_sim_sum)
NonMyo_sim_sum[index_zeros] = 0
NonMyo_sim_sum = np.repeat(np.matrix(NonMyo_sim_sum,),NonMyo_sim.shape[0], axis=0)
NonMyo_sim_out = np.multiply( NonMyo_sim,NonMyo_sim_sum)

collaborative_feature = np.vstack((Myo_sim_out,NonMyo_sim_out))
collaborative_sim = collaborative_feature.transpose()*collaborative_feature
collaborative_sim_norm =  np.matrix(np.sqrt(np.diag(collaborative_sim))).transpose() * np.matrix(np.sqrt(np.diag(collaborative_sim)))
collaborative_sim_norm = np.divide(collaborative_sim,collaborative_sim_norm)
collaborative_sim = collaborative_sim_norm

pdb.set_trace()
np.savetxt(OutputPath, collaborative_sim, delimiter=' ', fmt='%.4f')
