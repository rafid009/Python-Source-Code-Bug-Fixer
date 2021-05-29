import numpy as np 

def function(x):

	x3 = 2
	b0 = x
	paths = []
	try:
		if x3 > 3:
			b0 = x*5
			b0 = x/x3
			x = 1+x
			paths.append(1)
		else:
			x3 = x3*x3
			paths.append(2)
		if x3 <= 8:
			x3 = b0/3
			x3 = x3+5
			x3 = 0+b0
			paths.append(3)
		else:
			x = 9+6
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