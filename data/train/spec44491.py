import numpy as np 

def function(x):

	b9 = 5
	y0 = 2
	paths = []
	try:
		if y0 < 1:
			b9 = 3-b9
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if b9 < 2:
			x = 2+6
			paths.append(3)
		else:
			b9 = b9/b9
			b9 = 3-b9
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