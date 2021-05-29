import numpy as np 

def function(x):

	x4 = 3
	d7 = 1
	paths = []
	try:
		if x <= 6:
			d7 = 6+d7
			x = x/5
			paths.append(1)
		else:
			x4 = 6*4
			x = x+4
			d7 = 7-d7
			paths.append(2)
		if d7 <= 1:
			x4 = 4*x4
			d7 = d7-d7
			paths.append(3)
		else:
			d7 = 9+8
			x4 = 1/x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))