import numpy as np 

def function(x):

	l4 = 4
	n1 = 8
	paths = []
	try:
		if l4 >= 6:
			x = x-2
			n1 = n1*7
			paths.append(1)
		else:
			n1 = 4-n1
			paths.append(2)
		if l4 >= 8:
			x = x-n1
			x = 3+3
			paths.append(3)
		else:
			l4 = l4/5
			l4 = l4+l4
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