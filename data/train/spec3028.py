import numpy as np 

def function(x):

	n3 = 5
	x0 = x
	paths = []
	try:
		if x > 5:
			x = 6-x
			x = 4+x
			n3 = 5/x0
			paths.append(1)
		else:
			x0 = x0*x0
			x = 7*x
			x0 = x0*5
			paths.append(2)
		if n3 < 6:
			x = x0-n3
			x = x/x
			x = x-5
			paths.append(3)
		else:
			n3 = 2/3
			x = x/7
			x0 = 9*x
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