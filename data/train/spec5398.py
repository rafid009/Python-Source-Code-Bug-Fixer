import numpy as np 

def function(x):

	l6 = 0
	d8 = 8
	paths = []
	try:
		if d8 >= 2:
			d8 = d8*d8
			d8 = l6*d8
			x = d8+0
			paths.append(1)
		else:
			x = x*l6
			paths.append(2)
		if d8 < 7:
			d8 = d8-3
			x = d8-6
			paths.append(3)
		else:
			x = x/d8
			d8 = 4*d8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))