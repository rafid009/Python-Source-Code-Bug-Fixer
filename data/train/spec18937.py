import numpy as np 

def function(x):

	e8 = 0
	n4 = 7
	paths = []
	try:
		if x > 5:
			e8 = 8*e8
			n4 = n4+5
			e8 = n4-e8
			paths.append(1)
		else:
			n4 = 5/x
			paths.append(2)
		if e8 > 4:
			n4 = n4/x
			n4 = x+n4
			paths.append(3)
		else:
			e8 = 4*e8
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