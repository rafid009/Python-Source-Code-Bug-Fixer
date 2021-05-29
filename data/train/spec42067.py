import numpy as np 

def function(x):

	u7 = x
	d0 = 9
	paths = []
	try:
		if d0 < 7:
			u7 = u7*7
			paths.append(1)
		else:
			x = 6*d0
			d0 = d0*u7
			paths.append(2)
		if x <= 0:
			d0 = d0+3
			u7 = u7/8
			paths.append(3)
		else:
			x = 7/u7
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