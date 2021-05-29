import numpy as np 

def function(x):

	n0 = 7
	l6 = x
	paths = []
	try:
		if n0 <= 1:
			l6 = n0/4
			paths.append(1)
		else:
			n0 = n0/7
			n0 = x+9
			paths.append(2)
		if l6 < 6:
			n0 = x-5
			x = x+l6
			paths.append(3)
		else:
			n0 = 7+n0
			x = 9+4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))