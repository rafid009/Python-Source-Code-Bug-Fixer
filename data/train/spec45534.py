import numpy as np 

def function(x):

	a5 = x
	x5 = 4
	paths = []
	try:
		if x5 <= 7:
			x5 = x5-6
			paths.append(1)
		else:
			x5 = 5/x5
			paths.append(2)
		if x5 <= 1:
			a5 = a5+0
			paths.append(3)
		else:
			x5 = 5-0
			a5 = 7*a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))