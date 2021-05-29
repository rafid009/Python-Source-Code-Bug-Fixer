import numpy as np 

def function(x):

	d5 = x
	e7 = 9
	paths = []
	try:
		if x >= 0:
			d5 = 8-x
			e7 = 6/e7
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if d5 < 8:
			e7 = e7+8
			d5 = d5-5
			x = 8/e7
			paths.append(3)
		else:
			d5 = 8/9
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))