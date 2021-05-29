import numpy as np 

def function(x):

	x3 = 2
	b2 = 4
	paths = []
	try:
		if x3 >= 5:
			x3 = b2-x3
			b2 = b2*6
			paths.append(1)
		else:
			b2 = 9*x3
			x3 = 1-4
			x = x+b2
			paths.append(2)
		if b2 >= 9:
			x = x-x3
			x3 = x3+2
			x = x*2
			paths.append(3)
		else:
			x3 = 1/7
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