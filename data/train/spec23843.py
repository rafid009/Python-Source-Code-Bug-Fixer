import numpy as np 

def function(x):

	b0 = x
	x3 = 5
	paths = []
	try:
		if x > 3:
			x3 = x3*x
			x = x3+6
			paths.append(1)
		else:
			x3 = 0-b0
			paths.append(2)
		if b0 >= 1:
			x = b0-2
			x3 = 2+x
			paths.append(3)
		else:
			b0 = b0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))