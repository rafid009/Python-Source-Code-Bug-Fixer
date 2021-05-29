import numpy as np 

def function(x):

	n3 = x
	x0 = x
	paths = []
	try:
		if n3 >= 3:
			x0 = x0*x0
			n3 = 6-n3
			x0 = x0*x
			paths.append(1)
		else:
			x = n3+x0
			x = 4/x
			x = 2+x
			paths.append(2)
		if x >= 6:
			x = 1*7
			n3 = 7/n3
			n3 = x0-x0
			paths.append(3)
		else:
			n3 = n3/1
			x0 = x0+5
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