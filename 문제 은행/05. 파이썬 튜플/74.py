t = (1, 2, 3)
t[0] = 'a'
'''
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
'''

''' 오류가 나는 이유
튜플은 immutable한 자료형임
'''