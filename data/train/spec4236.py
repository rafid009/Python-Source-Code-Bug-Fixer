import numpy as np 

def function(x):

	l4 = x
	n7 = 3
	paths = []
	try:
		if x > 3:
			l4 = 1/5
			paths.append(1)
		else:
			n7 = n7/7
			x = x+n7
			paths.append(2)
		if x <= 0:
			n7 = 3+n7
			l4 = 7/2
			paths.append(3)
		else:
			n7 = 6-7
			n7 = n7/l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))