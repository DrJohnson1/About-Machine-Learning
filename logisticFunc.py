#! usr/bin/env python
# -*- coding:utf-8 -*-

import math
import numpy as np

scores = [-0.2,-3,1.5,0.05]

def f(x):
	return 1 / (1 + math.exp(-x))

logisticFunction = np.vectorize(f)

res = logisticFunction(np.array(scores))

import matplotlib.pyplot as plt 

x = np.arange(-4.0,4.0,0.1)

plt.plot(x,logisticFunction(x).T,linewidth=2)

plt.show()