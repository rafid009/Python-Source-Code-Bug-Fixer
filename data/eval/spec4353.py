import numpy as np 

def function(x):

	b4 = 4
	e2 = x
	paths = []
	try:
		if b4 > 5:
			b4 = b4-2
			paths.append(1)
		else:
			b4 = b4+3
			paths.append(2)
		if b4 > 4:
			x = 6-x
			paths.append(3)
		else:
			e2 = 7-b4
			x = 4/x
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