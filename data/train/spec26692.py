import numpy as np 

def function(x):

	j0 = 8
	x1 = x
	x = 5
	paths = []
	try:
		if x1 <= 3:
			x = x*7
			x = 1-j0
			paths.append(1)
		else:
			x1 = 3-8
			paths.append(2)
		if x <= 9:
			x1 = x/2
			x = 4*x
			paths.append(3)
		else:
			x = 5+3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))