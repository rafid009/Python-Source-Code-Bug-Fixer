import numpy as np 

def function(x):

	x4 = 1
	a5 = 7
	paths = []
	try:
		if x >= 8:
			a5 = 7*1
			paths.append(1)
		else:
			a5 = x+a5
			paths.append(2)
		if a5 >= 2:
			a5 = x-a5
			paths.append(3)
		else:
			x4 = 7-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))