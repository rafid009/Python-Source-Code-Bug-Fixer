import numpy as np 

def function(x):

	n6 = 3
	e1 = 8
	paths = []
	try:
		if x > 2:
			e1 = x-e1
			n6 = n6*e1
			paths.append(1)
		else:
			e1 = e1*5
			paths.append(2)
		if e1 <= 9:
			e1 = x/7
			x = 6/8
			x = 1+e1
			paths.append(3)
		else:
			n6 = 8*n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))