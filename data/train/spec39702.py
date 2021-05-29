import numpy as np 

def function(x):

	x0 = x
	u1 = 6
	x = 2
	paths = []
	try:
		if x0 <= 4:
			x = x0/6
			paths.append(1)
		else:
			x = 1*x
			x = 4-3
			x0 = 7-x0
			paths.append(2)
		if x0 < 5:
			u1 = 7/u1
			x0 = x0*8
			x = x-6
			paths.append(3)
		else:
			x = u1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))