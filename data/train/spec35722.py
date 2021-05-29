import numpy as np 

def function(x):

	q7 = 2
	x9 = x
	paths = []
	try:
		if x9 <= 0:
			x9 = x/3
			q7 = 6*x9
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if q7 >= 6:
			x9 = 5/x9
			paths.append(3)
		else:
			x9 = 0/x9
			q7 = q7-6
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