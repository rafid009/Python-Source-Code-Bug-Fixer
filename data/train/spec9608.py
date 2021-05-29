import numpy as np 

def function(x):

	k5 = 2
	n8 = 1
	paths = []
	try:
		if k5 >= 9:
			k5 = k5*n8
			n8 = x+n8
			k5 = k5*k5
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if k5 < 0:
			k5 = k5-1
			n8 = 6+4
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))