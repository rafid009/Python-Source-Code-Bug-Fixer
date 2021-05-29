import numpy as np 

def function(x):

	d4 = 6
	d1 = x
	paths = []
	try:
		if x > 3:
			d4 = d4/6
			x = 0-7
			d1 = d1-1
			paths.append(1)
		else:
			d1 = 4/d1
			paths.append(2)
		if x >= 5:
			d4 = 2/d4
			x = 0/x
			d4 = d4-4
			paths.append(3)
		else:
			d4 = 1+2
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