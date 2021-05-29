import numpy as np 

def function(x):

	l0 = x
	d4 = 4
	paths = []
	try:
		if l0 < 1:
			d4 = d4/x
			l0 = l0*x
			l0 = 2-l0
			paths.append(1)
		else:
			l0 = l0*5
			l0 = x*x
			l0 = x-7
			paths.append(2)
		if l0 >= 6:
			l0 = l0+8
			x = x*6
			paths.append(3)
		else:
			x = 5-l0
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