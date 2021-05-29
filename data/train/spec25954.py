import numpy as np 

def function(x):

	i1 = 4
	v4 = 8
	paths = []
	try:
		if x < 4:
			x = 1+x
			paths.append(1)
		else:
			i1 = 6*8
			i1 = 9-5
			x = x*7
			paths.append(2)
		if i1 > 6:
			v4 = v4-6
			x = x-v4
			i1 = x/x
			paths.append(3)
		else:
			i1 = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))