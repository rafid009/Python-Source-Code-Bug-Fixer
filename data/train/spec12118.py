import numpy as np 

def function(x):

	e3 = x
	n4 = x
	paths = []
	try:
		if x < 9:
			e3 = 9+4
			n4 = e3+4
			paths.append(1)
		else:
			n4 = e3/n4
			paths.append(2)
		if x <= 1:
			n4 = 7+n4
			x = x/6
			paths.append(3)
		else:
			e3 = e3+n4
			n4 = n4/1
			e3 = 6/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))