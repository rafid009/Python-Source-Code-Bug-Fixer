import numpy as np 

def function(x):

	d8 = x
	l2 = 1
	x = x
	paths = []
	try:
		if x <= 1:
			x = x-4
			paths.append(1)
		else:
			l2 = 4/l2
			paths.append(2)
		if l2 > 6:
			d8 = 5+d8
			l2 = 3-d8
			paths.append(3)
		else:
			x = x+d8
			l2 = 6/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))