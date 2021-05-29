import numpy as np 

def function(x):

	d2 = 7
	x8 = x
	paths = []
	try:
		if x > 3:
			d2 = d2+6
			x8 = x8/7
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x8 < 8:
			x = x+x8
			x = 8/x
			paths.append(3)
		else:
			d2 = x*d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))