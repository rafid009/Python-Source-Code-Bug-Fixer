import numpy as np 

def function(x):

	k1 = 8
	j7 = x
	paths = []
	try:
		if j7 <= 2:
			j7 = x-7
			x = 8/x
			paths.append(1)
		else:
			j7 = 1*j7
			x = 1/x
			k1 = 5/k1
			paths.append(2)
		if j7 > 2:
			x = 0-7
			k1 = 3/k1
			j7 = 2/8
			paths.append(3)
		else:
			x = 1*6
			j7 = 0*j7
			k1 = k1+6
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