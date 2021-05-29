import numpy as np 

def function(x):

	v1 = x
	l8 = 0
	paths = []
	try:
		if x >= 8:
			l8 = 1+0
			paths.append(1)
		else:
			l8 = 3-x
			x = x-2
			paths.append(2)
		if l8 >= 0:
			l8 = 7/2
			x = x/9
			l8 = l8/6
			paths.append(3)
		else:
			v1 = 0-v1
			x = 4/1
			l8 = l8/7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		l8 = v1**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))