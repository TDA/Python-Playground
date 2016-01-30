__author__ = 'saipc'

execfile("hello_world_2.py")
# is the same as:
exec(open("hello_world_2.py"))
# is also the same as
exec open("hello_world_2.py").read()
# is in Python 3 as:
exec(open("hello_world_2.py").read())