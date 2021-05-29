import numpy as np 

def function(x):

	x4 = 5
	d7 = 0
	paths = []
	try:
		if x4 <= 6:
			x = x4/x
			paths.append(1)
		else:
			x = d7*x
			x = d7-x
			paths.append(2)
		if d7 >= 5:
			x4 = 7*d7
			d7 = 6*d7
			d7 = d7/x4
			paths.append(3)
		else:
			x = x*x4
			x4 = x4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))