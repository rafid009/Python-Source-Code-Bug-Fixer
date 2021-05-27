import numpy as np 

def function(x):

	a7 = x
	n4 = x
	paths = []
	try:
		if x <= 9:
			n4 = n4/n4
			paths.append(1)
		else:
			x = 1/x
			n4 = a7/2
			paths.append(2)
		if a7 > 7:
			x = 8*x
			x = x+4
			paths.append(3)
		else:
			a7 = a7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))