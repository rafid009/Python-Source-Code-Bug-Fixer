import numpy as np 

def function(x):

	n1 = x
	x3 = 9
	paths = []
	try:
		if x3 > 9:
			x3 = 1-8
			n1 = 0/x
			paths.append(1)
		else:
			x = 8/x
			x3 = 7-x3
			x3 = 1+x3
			paths.append(2)
		if x < 3:
			x = 1*x
			n1 = 2*n1
			x = 4-7
			paths.append(3)
		else:
			x = x-x
			x = 4/4
			n1 = n1/7
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