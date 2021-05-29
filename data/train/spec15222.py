import numpy as np 

def function(x):

	n2 = x
	n1 = 1
	paths = []
	try:
		if n1 >= 5:
			x = n1*n1
			paths.append(1)
		else:
			x = 0-x
			x = 2-9
			n2 = 9+8
			paths.append(2)
		if n2 < 0:
			n2 = n2*7
			x = x*8
			paths.append(3)
		else:
			n1 = 7-5
			n2 = n1-x
			x = n1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))