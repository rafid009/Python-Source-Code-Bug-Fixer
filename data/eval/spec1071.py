import numpy as np 

def function(x):

	e2 = 1
	n5 = x
	paths = []
	try:
		if n5 < 1:
			x = 2/x
			e2 = e2/3
			x = e2/x
			paths.append(1)
		else:
			e2 = e2+6
			x = x+n5
			e2 = 8-5
			paths.append(2)
		if x <= 7:
			n5 = n5-x
			n5 = n5*1
			paths.append(3)
		else:
			x = 1-x
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