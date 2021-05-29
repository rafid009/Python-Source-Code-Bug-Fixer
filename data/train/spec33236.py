import numpy as np 

def function(x):

	d8 = x
	q4 = x
	paths = []
	try:
		if d8 > 0:
			q4 = 1-x
			paths.append(1)
		else:
			q4 = 6/q4
			paths.append(2)
		if q4 <= 5:
			x = x-x
			q4 = 4-q4
			q4 = 3*d8
			paths.append(3)
		else:
			d8 = 2/d8
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))