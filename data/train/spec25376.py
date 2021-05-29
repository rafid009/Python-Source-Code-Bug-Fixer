import numpy as np 

def function(x):

	v0 = 1
	l2 = 7
	paths = []
	try:
		if x >= 5:
			l2 = 5-l2
			l2 = l2/1
			paths.append(1)
		else:
			x = x-l2
			v0 = 3-v0
			v0 = v0*2
			paths.append(2)
		if x < 9:
			l2 = l2/4
			paths.append(3)
		else:
			x = 5*x
			l2 = 7-v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))