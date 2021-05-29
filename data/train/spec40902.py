import numpy as np 

def function(x):

	x9 = 7
	b8 = 2
	paths = []
	try:
		if x < 2:
			x9 = x9/x9
			b8 = 1-1
			b8 = b8+b8
			paths.append(1)
		else:
			x9 = 1*x9
			paths.append(2)
		if b8 <= 8:
			x = x9/x
			x9 = 0*3
			paths.append(3)
		else:
			x = 6/x
			b8 = 0*b8
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