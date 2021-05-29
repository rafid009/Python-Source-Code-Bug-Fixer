import numpy as np 

def function(x):

	j5 = 0
	x0 = x
	paths = []
	try:
		if j5 < 1:
			x = 4-j5
			paths.append(1)
		else:
			x0 = 2*x0
			x = 2+j5
			paths.append(2)
		if j5 < 0:
			j5 = 6*j5
			j5 = j5*x0
			paths.append(3)
		else:
			x = x/x
			j5 = x0-j5
			j5 = 6-1
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))