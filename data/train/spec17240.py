import numpy as np 

def function(x):

	d4 = 4
	l0 = 2
	paths = []
	try:
		if d4 < 6:
			l0 = l0-7
			paths.append(1)
		else:
			l0 = 4-d4
			x = 7/x
			x = x*x
			paths.append(2)
		if x < 3:
			d4 = 7*6
			d4 = d4*d4
			paths.append(3)
		else:
			x = x-l0
			d4 = 1-2
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))