import numpy as np 

def function(x):

	e7 = x
	n4 = x
	paths = []
	try:
		if e7 >= 1:
			e7 = 8-e7
			e7 = x*2
			paths.append(1)
		else:
			x = x*n4
			paths.append(2)
		if n4 < 0:
			x = x+n4
			e7 = e7/x
			n4 = e7+n4
			paths.append(3)
		else:
			x = x/e7
			e7 = n4-e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))