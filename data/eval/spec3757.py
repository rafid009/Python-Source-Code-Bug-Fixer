import numpy as np 

def function(x):

	q7 = x
	x9 = 2
	paths = []
	try:
		if x9 >= 8:
			q7 = q7-3
			x = 2-x
			paths.append(1)
		else:
			x9 = x9+5
			paths.append(2)
		if x <= 7:
			q7 = q7+9
			paths.append(3)
		else:
			x9 = 1/x9
			q7 = q7*9
			x9 = x9*q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))