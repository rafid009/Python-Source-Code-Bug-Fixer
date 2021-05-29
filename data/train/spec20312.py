import numpy as np 

def function(x):

	d5 = x
	x5 = 0
	paths = []
	try:
		if x5 < 7:
			d5 = 9+d5
			x5 = x5/d5
			x = x-0
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x5 <= 1:
			x = x+0
			paths.append(3)
		else:
			x = x5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))