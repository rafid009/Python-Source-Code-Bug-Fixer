import numpy as np 

def function(x):

	u1 = x
	d5 = x
	paths = []
	try:
		if d5 < 5:
			u1 = u1/x
			paths.append(1)
		else:
			d5 = 9*d5
			d5 = d5/u1
			paths.append(2)
		if u1 < 5:
			x = 0-x
			d5 = d5+u1
			u1 = 8/6
			paths.append(3)
		else:
			d5 = d5*6
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