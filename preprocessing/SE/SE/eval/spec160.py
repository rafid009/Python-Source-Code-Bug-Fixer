import numpy as np 

def function(x):

	d8 = x
	q7 = 8
	paths = []
	try:
		if q7 < 6:
			x = 4/3
			paths.append(1)
		else:
			x = x*d8
			paths.append(2)
		if d8 >= 4:
			d8 = 4/q7
			q7 = d8+6
			paths.append(3)
		else:
			x = 0-q7
			d8 = d8+2
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