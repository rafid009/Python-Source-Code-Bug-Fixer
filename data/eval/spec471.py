import numpy as np 

def function(x):

	l5 = x
	n4 = x
	paths = []
	try:
		if x > 1:
			l5 = 8+l5
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if x >= 6:
			n4 = n4/4
			x = l5+0
			x = 3/x
			paths.append(3)
		else:
			l5 = n4*8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))