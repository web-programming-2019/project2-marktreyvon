import random

# a = str(int(random.random()*(10**10)))
a = random.randrange(99,999)
print(a)

import datetime,time as t
#
# # a = datetime.datetime()
# print()
# print(t.ctime())
# print(t.time())
# print(t.gmtime())
# print(t.asctime())
# print(t.localtime())
# help(t.time)

# print(t.strftime("%Y-%m-%d-%H:%M:%S",t.localtime()))
#
# def a():
#     print(1)
#     return 123,4
# q,w = a()
# print(q,w)
#
import json

a = [['a'],['d']]
print(a)
print(json.dumps(a))