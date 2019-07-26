# -*- coding: utf-8 -*-
# @Author: hsz
# @Date:   2019-07-11 21:10:06
# @Last Modified by:   hsz
# @Last Modified time: 2019-07-11 21:33:09

import sqlite3
import os

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()  # 创建游标
c.execute('SELECT * FROM review_db WHERE data'
          " BETWEEN '2019-01-01 00:00:00' AND DATETIME('now')")

results = c.fetchall()
print(results)
conn.close()