import numpy as np 

def function(x):

	k4 = 4
	b6 = 6
	paths = []
	try:
		if x > 7:
			x = 0-1
			x = x-0
			k4 = k4-2
			paths.append(1)
		else:
			b6 = b6/k4
			paths.append(2)
		if k4 >= 6:
			k4 = k4*4
			paths.append(3)
		else:
			x = 8*x
			k4 = k4/2
			b6 = b6-5
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