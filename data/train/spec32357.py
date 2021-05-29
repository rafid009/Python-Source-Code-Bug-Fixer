import numpy as np 

def function(x):

	d6 = x
	l2 = x
	paths = []
	try:
		if d6 <= 4:
			l2 = 4-l2
			x = d6-2
			paths.append(1)
		else:
			l2 = 2-l2
			l2 = 4*l2
			l2 = 8/l2
			paths.append(2)
		if d6 >= 6:
			l2 = x/5
			paths.append(3)
		else:
			d6 = 7/d6
			l2 = 2-6
			x = d6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))