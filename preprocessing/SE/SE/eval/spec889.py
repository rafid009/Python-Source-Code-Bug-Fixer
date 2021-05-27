import numpy as np 

def function(x):

	w7 = 4
	k0 = x
	paths = []
	try:
		if x < 0:
			w7 = k0+w7
			paths.append(1)
		else:
			k0 = 1-k0
			x = 3-7
			paths.append(2)
		if k0 >= 4:
			w7 = w7/7
			x = x-k0
			x = 7-1
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))