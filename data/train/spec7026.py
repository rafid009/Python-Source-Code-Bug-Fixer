import numpy as np 

def function(x):

	x2 = 0
	a3 = x
	paths = []
	try:
		if a3 > 7:
			x2 = x2*1
			x = 8*x
			x2 = 4-x2
			paths.append(1)
		else:
			a3 = 6/a3
			paths.append(2)
		if x >= 3:
			x = x/1
			paths.append(3)
		else:
			a3 = 4+a3
			a3 = 5+a3
			a3 = x2*a3
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