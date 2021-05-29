import numpy as np 

def function(x):

	l4 = 3
	z6 = x
	paths = []
	try:
		if z6 >= 4:
			l4 = 0-z6
			l4 = 2/8
			l4 = l4/x
			paths.append(1)
		else:
			l4 = 6/l4
			l4 = 2/l4
			paths.append(2)
		if z6 >= 0:
			x = x-3
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))