import numpy as np 

def function(x):

	l2 = 2
	d8 = 5
	paths = []
	try:
		if d8 <= 6:
			d8 = d8/5
			d8 = l2/d8
			paths.append(1)
		else:
			l2 = d8-l2
			d8 = 5*4
			paths.append(2)
		if x <= 9:
			x = x/6
			paths.append(3)
		else:
			x = 4*x
			l2 = d8-2
			l2 = d8-l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))