import numpy as np 

def function(x):

	b5 = 4
	b1 = 2
	paths = []
	try:
		if x <= 9:
			x = 6/x
			b5 = 4*b5
			x = b1/x
			paths.append(1)
		else:
			x = x+3
			x = b1*x
			b5 = 8+5
			paths.append(2)
		if b5 < 6:
			b1 = 1/x
			b5 = 6*b5
			paths.append(3)
		else:
			x = x*5
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