import numpy as np 

def function(x):

	f4 = 0
	x1 = 5
	paths = []
	try:
		if f4 > 8:
			x1 = 2/x1
			x1 = x1-x1
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if x1 > 8:
			x = 5+9
			x1 = 4*x1
			paths.append(3)
		else:
			x1 = x1-0
			x1 = x1*1
			x = 7-9
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