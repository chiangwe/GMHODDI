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
from sklearn.metrics.pairwise import rbf_kernel
import math
from sklearn import svm
import time
from parse import csr_parse

##############################################
#Parameter for tanimoto order
##############################################

print "======================================"
print "Common Drugs"
print "python Kernel_CommonDrugs.py order ./DrugComb_path ./Output_path"
print "======================================"


para = []
for arg in sys.argv:
        print arg
        para.append(arg)

order = int(para[1])
DrugCmbPath = para[2]
OutputPath = para[3]

if len(para) != 4 :
        exit()

All_sets_drug = lil_matrix( csr_parse(DrugCmbPath) );
All_sets_num = All_sets_drug.shape[0]


def tanimoto (list1, list2):
        number_of_intersect = float( len( set(list1) & set(list2) ) )
        number_of_diff = float( len(list1) + len(list2) - number_of_intersect )
        if number_of_diff == 0:
                return 0
        else:
                return number_of_intersect / number_of_diff
if( order == 1):
	All_data = All_sets_drug	
	All_data = sparse.vstack(  (  lil_matrix(np.zeros((1,All_data.shape[1]))) ,All_data )  )
	All_data = sparse.hstack(  (  lil_matrix(np.zeros((All_data.shape[0],1))) ,All_data )  )
	All_data = lil_matrix(All_data)
elif(order == 2):
	All_data = All_sets_drug
	Order_max = 2
	com_sets = []
	for rows in range(0,len(All_data.rows)):
		temp =[]
		for Order in range(1,Order_max+1):
			temp.append( [tuple(x) for x in itertools.combinations(All_data.rows[rows], Order)] )
		com_sets.append( list(itertools.chain(*temp)) )
	com    = set(itertools.chain(*com_sets))
        All_sets = com
        All_sets = list(All_sets)

	All_feature_dict = {};
	index = 1
	for sets in All_sets :
		All_feature_dict[sets] = index
		index = index + 1
	
	All_data_feature_drug = lil_matrix((All_data.shape[0],len(All_feature_dict)+1));
	All_data_feature_drug_rows = []
	All_data_feature_drug_datas = []
	for feature in com_sets:
		rows = [All_feature_dict[i] for i in feature ]
		All_data_feature_drug_rows.append( rows )
		All_data_feature_drug_datas.append([1]*len(rows))
	
	All_data_feature_drug.data = array(All_data_feature_drug_datas)
	All_data_feature_drug.rows = array(All_data_feature_drug_rows)
	All_data = All_data_feature_drug

intersection = ( All_data*All_data.transpose() ).todense()

sum_all = All_data.sum(1)
sum_all = np.tile(sum_all,(1,All_data.shape[0]))
sum_all = np.add( np.add( sum_all,  sum_all.transpose() )  , -intersection )

zero_posit = np.where(sum_all == 0)
intersection[zero_posit] = 0
sum_all[zero_posit] = 1
Tani_sim_out = np.divide( intersection , sum_all )
np.savetxt(OutputPath, Tani_sim_out, delimiter=' ', fmt='%.10f')

                                                      
