import numpy as np 

def function(x):

	x3 = x
	x5 = 3
	paths = []
	try:
		if x3 > 1:
			x5 = x5*x5
			x3 = 8*5
			x = x-x
			paths.append(1)
		else:
			x5 = x5+x5
			x = x5-x
			paths.append(2)
		if x > 3:
			x5 = x5*3
			paths.append(3)
		else:
			x3 = 7*x3
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x5 = x3**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))