import numpy as np 

def function(x):

	l6 = 9
	d5 = 7
	paths = []
	try:
		if d5 <= 6:
			l6 = 1-d5
			d5 = d5*4
			paths.append(1)
		else:
			d5 = x+d5
			paths.append(2)
		if l6 < 1:
			l6 = 7/3
			paths.append(3)
		else:
			d5 = 4/d5
			d5 = d5-4
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))