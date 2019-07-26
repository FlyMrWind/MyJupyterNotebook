# -*- coding: utf-8 -*-
# @Author: hsz
# @Date:   2019-07-11 19:07:59
# @Last Modified by:   hsz
# @Last Modified time: 2019-07-11 20:49:49

import pickle
import re
import os
from vectorizer import vect
import numpy as np

clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))
label = {0: 'negative', 1: 'positive'}  # 类标字典
example = ['I love this movie']
X = vect.transform(example) # clf.predict()返回类标，clf.predict_proba()返回概率矩阵，np.max()返回概率矩阵里的最大值
print('Prediction: %s\nProbabality: %.2f' % (label[clf.predict(X)[0]], np.max(clf.predict_proba(X)) * 100))
