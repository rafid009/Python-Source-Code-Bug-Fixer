import numpy as np 

def function(x):

	o0 = x
	x0 = 1
	paths = []
	try:
		if x0 >= 5:
			x = x-x0
			paths.append(1)
		else:
			o0 = x0/6
			paths.append(2)
		if x >= 2:
			x0 = 7/2
			o0 = 9-x0
			paths.append(3)
		else:
			x = x+6
			x0 = x0+x
			x0 = 1-9
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