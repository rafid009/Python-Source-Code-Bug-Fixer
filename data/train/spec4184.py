import numpy as np 

def function(x):

	y8 = 2
	e8 = x
	paths = []
	try:
		if x <= 2:
			x = x-8
			y8 = x-5
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if y8 <= 0:
			e8 = x-x
			e8 = e8-4
			x = 1+x
			paths.append(3)
		else:
			x = 2*x
			x = x-y8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))