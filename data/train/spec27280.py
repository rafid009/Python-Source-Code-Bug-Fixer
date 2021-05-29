import numpy as np 

def function(x):

	x4 = x
	k2 = x
	paths = []
	try:
		if x4 > 5:
			k2 = k2+0
			x = 3-x
			k2 = 2-5
			paths.append(1)
		else:
			k2 = k2-2
			paths.append(2)
		if x4 < 1:
			k2 = k2*1
			k2 = x/2
			paths.append(3)
		else:
			x = x4*x
			x = k2-7
			x4 = x-k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))