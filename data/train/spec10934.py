import numpy as np 

def function(x):

	l4 = x
	x6 = x
	paths = []
	try:
		if x <= 8:
			l4 = l4/x
			paths.append(1)
		else:
			x = 2*x
			x6 = x+l4
			paths.append(2)
		if x6 >= 9:
			l4 = l4-x6
			paths.append(3)
		else:
			x6 = x6*4
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))