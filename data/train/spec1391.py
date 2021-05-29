import numpy as np 

def function(x):

	q0 = x
	d4 = 9
	paths = []
	try:
		if d4 > 9:
			q0 = 3-q0
			d4 = 1*q0
			paths.append(1)
		else:
			q0 = q0/9
			paths.append(2)
		if d4 > 0:
			d4 = q0/3
			paths.append(3)
		else:
			q0 = q0*d4
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))