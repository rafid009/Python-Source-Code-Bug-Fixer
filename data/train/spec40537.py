import numpy as np 

def function(x):

	x9 = x
	j5 = 5
	x = x
	paths = []
	try:
		if j5 > 3:
			j5 = x9-0
			paths.append(1)
		else:
			x9 = x9*7
			x9 = x9+x
			x9 = x9+3
			paths.append(2)
		if x9 >= 1:
			x = x-4
			paths.append(3)
		else:
			x9 = 7+x9
			x = 8/x
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