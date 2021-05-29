import numpy as np 

def function(x):

	k1 = x
	x7 = 6
	paths = []
	try:
		if x7 > 1:
			k1 = k1*k1
			x7 = 8+x7
			paths.append(1)
		else:
			k1 = 8/k1
			paths.append(2)
		if x7 <= 9:
			k1 = 2*1
			paths.append(3)
		else:
			x7 = k1/7
			x7 = x7/1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))