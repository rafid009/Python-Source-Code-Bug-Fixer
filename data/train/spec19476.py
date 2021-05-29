import numpy as np 

def function(x):

	d9 = x
	l2 = x
	paths = []
	try:
		if l2 < 3:
			x = x/x
			l2 = d9-2
			x = 0-8
			paths.append(1)
		else:
			l2 = l2-0
			paths.append(2)
		if x >= 6:
			d9 = 7+d9
			paths.append(3)
		else:
			l2 = l2+l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))