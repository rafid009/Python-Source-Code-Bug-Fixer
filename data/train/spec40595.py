import numpy as np 

def function(x):

	x0 = 3
	u5 = 1
	paths = []
	try:
		if x < 8:
			u5 = u5-7
			x0 = 2-x0
			x = 3+x
			paths.append(1)
		else:
			x = x*x0
			x = 9*x
			x0 = 8*u5
			paths.append(2)
		if x > 6:
			x = x-6
			paths.append(3)
		else:
			x0 = x0-x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))