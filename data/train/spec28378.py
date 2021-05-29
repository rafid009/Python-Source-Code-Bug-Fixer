import numpy as np 

def function(x):

	l2 = 5
	h8 = x
	x = 5
	paths = []
	try:
		if h8 > 2:
			l2 = 0*l2
			paths.append(1)
		else:
			l2 = l2+4
			l2 = 0+l2
			paths.append(2)
		if h8 < 7:
			x = x*4
			x = 7+x
			paths.append(3)
		else:
			x = 8-h8
			l2 = 4/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))