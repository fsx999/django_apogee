# coding=utf-8
from __future__ import unicode_literals
import re
f = open('models_individu.py', 'r')


def toto(m):
    return m.group(0).lower()

result = []

for line in f.readlines():
    result.append(re.sub(r'^.* = ', toto, line))

f.close()
f = open('models_individu.py', 'w')
for x in result:
    f.write(x)
f.close()


