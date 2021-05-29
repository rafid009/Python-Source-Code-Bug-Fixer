import numpy as np 

def function(x):

	x3 = 2
	k4 = 5
	paths = []
	try:
		if x > 1:
			x3 = k4/x3
			x = x*x3
			x3 = x3/6
			paths.append(1)
		else:
			x3 = x3*k4
			k4 = k4*6
			paths.append(2)
		if k4 <= 6:
			k4 = k4+1
			paths.append(3)
		else:
			x3 = x+3
			x3 = x3-0
			k4 = k4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))