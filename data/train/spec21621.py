import numpy as np 

def function(x):

	n1 = x
	n6 = 0
	paths = []
	try:
		if n1 < 4:
			x = x-1
			paths.append(1)
		else:
			n1 = n6*6
			n1 = n1/x
			x = x*3
			paths.append(2)
		if x <= 1:
			n6 = 3*x
			paths.append(3)
		else:
			x = 4*n1
			x = 5+x
			n6 = n1*x
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