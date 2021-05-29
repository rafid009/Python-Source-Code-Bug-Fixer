import numpy as np 

def function(x):

	x1 = 6
	s1 = x
	paths = []
	try:
		if x >= 5:
			x = x-9
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x >= 7:
			x1 = 1*x1
			paths.append(3)
		else:
			x1 = x1/9
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