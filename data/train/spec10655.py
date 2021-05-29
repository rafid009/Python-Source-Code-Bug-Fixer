import numpy as np 

def function(x):

	k4 = 2
	h5 = 9
	paths = []
	try:
		if k4 <= 9:
			x = x-0
			k4 = 7-k4
			paths.append(1)
		else:
			k4 = 5+3
			h5 = k4/5
			paths.append(2)
		if k4 > 9:
			x = k4/x
			k4 = 0+k4
			paths.append(3)
		else:
			k4 = k4-4
			k4 = 0+5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))