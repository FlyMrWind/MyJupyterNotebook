# -*- coding: utf-8 -*-
# @Author: hsz
# @Date:   2019-07-11 20:51:28
# @Last Modified by:   hsz
# @Last Modified time: 2019-07-11 21:20:52

import sqlite3
import os

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()

# 没有文件覆盖，需要删除以后才能再次执行程序
c.execute('CREATE TABLE review_db'
          '(review TEXT, sentiment INTEGER, data TEXT)')

example1 = 'I love this movie.'

c.execute("INSERT INTO review_db"
          "(review, sentiment, data) VALUES"
          "(?, ?, DATETIME('now'))", (example1, 1))

example2 = 'I dislike this movie.'

c.execute("INSERT INTO review_db"
          "(review, sentiment, data) VALUES"
          "(?, ?, DATETIME('now'))", (example2, 0))

conn.commit()
conn.close()
