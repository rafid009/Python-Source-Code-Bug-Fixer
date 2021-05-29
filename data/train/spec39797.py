import numpy as np 

def function(x):

	n1 = 8
	e1 = 8
	paths = []
	try:
		if n1 >= 5:
			n1 = 1+3
			paths.append(1)
		else:
			x = 0*7
			x = 1-e1
			paths.append(2)
		if e1 >= 4:
			n1 = n1-2
			n1 = n1-e1
			paths.append(3)
		else:
			x = n1+n1
			x = 9+x
			n1 = e1+e1
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