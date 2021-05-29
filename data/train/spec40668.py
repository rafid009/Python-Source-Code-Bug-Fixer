import numpy as np 

def function(x):

	d0 = 0
	x9 = 8
	paths = []
	try:
		if x < 8:
			d0 = x+d0
			d0 = d0-x
			d0 = 8-d0
			paths.append(1)
		else:
			d0 = d0+1
			paths.append(2)
		if x < 3:
			x9 = x9+x9
			d0 = d0/x
			x = x+d0
			paths.append(3)
		else:
			x = 4/3
			d0 = 3-0
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