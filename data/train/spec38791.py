import numpy as np 

def function(x):

	e6 = x
	n1 = x
	paths = []
	try:
		if n1 <= 6:
			n1 = 6*n1
			e6 = e6+5
			paths.append(1)
		else:
			e6 = e6/x
			paths.append(2)
		if x < 2:
			x = e6/x
			x = 6+x
			paths.append(3)
		else:
			x = 2+n1
			e6 = e6+e6
			n1 = n1+n1
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