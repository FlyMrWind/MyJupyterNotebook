# -*- coding: utf-8 -*-
# @Author: hsz
# @Date:   2019-07-12 20:02:10
# @Last Modified by:   hsz
# @Last Modified time: 2019-07-12 22:20:27

import pickle
import sqlite3
import numpy as np
import os

# import HasingVectorizer from local dir
from vectorizer import vect


def updata_model(db_path, model, batch_size=10000):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from review_db')

    results = c.fetchmany(batch_size)
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)

        classes = np.array([0, 1])
        X_train = vect.transform(X)
        clf.partial_fit(X_train, y, classes=classes)
        results = c.fetchmany(batch_size)
    conn.close()
    return None


cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

updata_model(db_path=db, model=clf, batch_size=10000)

# Uncomment the following lines if you are sure that
# you want to updata your classifier.pkl file permanently

# pickle.dump(clf, open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'wb'), protocol=4)
