import numpy as np 

def function(x):

	v8 = 0
	l4 = 7
	paths = []
	try:
		if x >= 1:
			v8 = v8*3
			paths.append(1)
		else:
			l4 = 6/l4
			paths.append(2)
		if x >= 1:
			l4 = 4+l4
			v8 = 7+l4
			paths.append(3)
		else:
			x = 1*x
			l4 = v8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))