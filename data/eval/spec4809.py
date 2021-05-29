import numpy as np 

def function(x):

	j4 = 2
	x4 = 2
	paths = []
	try:
		if j4 > 0:
			x4 = x4/2
			paths.append(1)
		else:
			x4 = x4-6
			paths.append(2)
		if x4 <= 3:
			x4 = x4+6
			x = x*4
			j4 = 2/j4
			paths.append(3)
		else:
			j4 = j4*7
			x4 = x*x4
			x4 = x4*j4
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