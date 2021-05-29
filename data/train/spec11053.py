import numpy as np 

def function(x):

	l8 = 5
	v7 = 2
	paths = []
	try:
		if x <= 1:
			l8 = l8/l8
			paths.append(1)
		else:
			v7 = v7*1
			x = 4/x
			paths.append(2)
		if v7 > 6:
			l8 = l8*l8
			v7 = v7/v7
			v7 = v7+x
			paths.append(3)
		else:
			v7 = v7/7
			l8 = 1-l8
			x = 0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))