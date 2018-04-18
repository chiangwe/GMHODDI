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
#Parameter for Single Drug Similarity 
##############################################

print "======================================"
print "Drug combination kernel from drug similarity"
print "python Kernel_DrugSimilarity.py ./SDS_path ./DrugComb_path ./Output_path"
print "======================================"


para = []
for arg in sys.argv:
        print arg
        para.append(arg)

SimPath = para[1]
DrugCmbPath = para[2]
OutputPath = para[3]

if len(para) != 4 : 
	exit()

##############################################
#reading Input
##############################################

Drug_sim = np.loadtxt(SimPath);
All_sets_drug = lil_matrix( csr_parse(DrugCmbPath) ); 
All_sets_num = All_sets_drug.shape[0]

#############################################
#Graph Matching
############################################

index_x = 0
index_y = All_sets_drug.shape[0]-1

set_sim = np.zeros( ( index_y-index_x+1 ,All_sets_num ) )

for i in range(0, All_sets_num):
        for j in range(i, All_sets_num ):
		Sim_total = 0
		Comb_I = list( All_sets_drug[i,:].rows[0] )
		Comb_J = list( All_sets_drug[j,:].rows[0] )
		Drug_sunsim = Drug_sim[Comb_I,:]
		Drug_sunsim = Drug_sunsim[:,Comb_J]
		for tuples in itertools.product(Comb_I,Comb_J):
			Sim_total = Sim_total + Drug_sim[tuples]
		similarity_sum_avg = Sim_total/(len(Comb_I)*len(Comb_J))
		set_sim[i-index_x,j] = similarity_sum_avg
		print "Set sim on " + str(i)+" and " + str(j)
np.savetxt(OutputPath, set_sim, delimiter=' ', fmt='%.4f')
