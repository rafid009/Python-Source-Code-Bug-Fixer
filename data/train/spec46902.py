import numpy as np 

def function(x):

	n5 = 8
	l8 = x
	paths = []
	try:
		if x >= 5:
			l8 = l8+4
			paths.append(1)
		else:
			l8 = 2*l8
			paths.append(2)
		if x < 8:
			x = x*x
			paths.append(3)
		else:
			x = 3-l8
			x = x/1
			l8 = 3+3
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		n5 = l8**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))