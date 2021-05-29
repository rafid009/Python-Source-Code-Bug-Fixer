import numpy as np 

def function(x):

	x3 = x
	b5 = 2
	paths = []
	try:
		if x > 7:
			x3 = 5/b5
			b5 = 6*x
			paths.append(1)
		else:
			b5 = b5*b5
			x = x3-6
			paths.append(2)
		if x > 4:
			x = 9/x
			x = 2-3
			paths.append(3)
		else:
			x = x*b5
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