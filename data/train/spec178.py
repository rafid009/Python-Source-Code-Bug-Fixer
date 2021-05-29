import numpy as np 

def function(x):

	d8 = x
	q0 = 0
	paths = []
	try:
		if d8 <= 0:
			q0 = 4*q0
			q0 = 8-x
			paths.append(1)
		else:
			d8 = d8+d8
			q0 = q0-5
			q0 = 2-q0
			paths.append(2)
		if q0 <= 2:
			q0 = q0/x
			paths.append(3)
		else:
			d8 = d8+d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))