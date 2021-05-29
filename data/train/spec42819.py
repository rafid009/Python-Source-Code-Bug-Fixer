import numpy as np 

def function(x):

	x3 = x
	x0 = 7
	paths = []
	try:
		if x3 >= 6:
			x3 = x3+0
			x0 = x0*x
			x = x+8
			paths.append(1)
		else:
			x3 = x3/5
			x3 = 7+x
			paths.append(2)
		if x < 8:
			x = x+x
			x3 = 1+x3
			paths.append(3)
		else:
			x = x+x0
			x0 = x0/2
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x0 = x3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))