import numpy as np 

def function(x):

	n1 = 7
	l2 = 0
	x = x
	paths = []
	try:
		if x < 4:
			x = 0/x
			x = n1/4
			paths.append(1)
		else:
			x = 4+x
			x = x*3
			paths.append(2)
		if x > 8:
			n1 = 8+n1
			l2 = 5*l2
			x = 2/x
			paths.append(3)
		else:
			x = 0-x
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