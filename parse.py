import pdb
from numpy  import array
import cPickle as pickle
from copy import deepcopy
from scipy.sparse import *
import numpy as np
from scipy import sparse
import cPickle
import random
import scipy.io as sio
import math
import shelve
from collections import Counter
import itertools
import multiprocessing
import sys
import math


def csr_parse(path):
	row = [];
	col = [];
	filePtr = open(path,'r')
	print path
	Drug_Num = int(filePtr.readline())
	line = filePtr.readline()
	indx = 0;
	while line :
		co = [ int(number) for number in line.split('\n')[0].split(' ') ]
		ro = [indx]*len(co);
		row = row + ro;
		col = col + co;
		line = filePtr.readline()
		indx = indx + 1;
	filePtr.close()
	Drug_sparse = csr_matrix(( np.ones((1,len(row)))[0] , (np.array(row), np.array(col)) ), shape=(indx, Drug_Num))
	return Drug_sparse






