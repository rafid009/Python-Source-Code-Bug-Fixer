import numpy as np 

def function(x):

	n1 = 9
	q7 = x
	paths = []
	try:
		if n1 < 8:
			n1 = 0/n1
			n1 = n1*n1
			n1 = 3+4
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x > 9:
			x = n1-7
			paths.append(3)
		else:
			n1 = n1-n1
			x = 5-x
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