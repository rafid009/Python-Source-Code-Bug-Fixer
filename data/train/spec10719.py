import numpy as np 

def function(x):

	i1 = 5
	x7 = 6
	paths = []
	try:
		if i1 > 3:
			x7 = x7*x
			x7 = x7/x
			x7 = 6/2
			paths.append(1)
		else:
			x7 = x7+x7
			paths.append(2)
		if x < 8:
			i1 = x7-x
			paths.append(3)
		else:
			x = 0+x7
			i1 = x7+i1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))