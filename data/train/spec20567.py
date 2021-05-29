import numpy as np 

def function(x):

	n8 = 3
	a3 = x
	paths = []
	try:
		if x >= 9:
			n8 = n8*x
			paths.append(1)
		else:
			n8 = 1/9
			paths.append(2)
		if x < 1:
			n8 = n8*x
			n8 = n8/a3
			paths.append(3)
		else:
			x = x*n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))