import numpy as np 

def function(x):

	l4 = 3
	x1 = 1
	paths = []
	try:
		if x1 >= 0:
			x = 9*x
			l4 = l4*9
			l4 = 1*x1
			paths.append(1)
		else:
			x = x1/x1
			x1 = x1+x1
			x = 4+5
			paths.append(2)
		if x1 > 5:
			l4 = 7*x
			paths.append(3)
		else:
			l4 = l4+x1
			x = x+x
			x = x1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))