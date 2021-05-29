import numpy as np 

def function(x):

	x3 = 5
	p8 = x
	paths = []
	try:
		if x3 < 7:
			x3 = x3+7
			p8 = p8/2
			paths.append(1)
		else:
			x = p8*3
			x3 = 5+3
			x3 = x*x3
			paths.append(2)
		if x < 9:
			p8 = 1-4
			paths.append(3)
		else:
			x = p8-9
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