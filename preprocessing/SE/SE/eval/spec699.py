import numpy as np 

def function(x):

	n8 = x
	l8 = x
	x = 4
	paths = []
	try:
		if x > 3:
			n8 = l8*n8
			paths.append(1)
		else:
			l8 = 0/l8
			paths.append(2)
		if n8 < 3:
			n8 = x/x
			x = x-x
			n8 = x+n8
			paths.append(3)
		else:
			l8 = 7+l8
			x = l8*x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		n8 = l8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))