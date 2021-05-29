import numpy as np 

def function(x):

	q4 = x
	d4 = 6
	paths = []
	try:
		if q4 < 5:
			x = x*x
			d4 = 5/d4
			x = d4*9
			paths.append(1)
		else:
			x = d4/3
			paths.append(2)
		if d4 >= 0:
			d4 = 3*d4
			x = x*q4
			paths.append(3)
		else:
			q4 = q4+4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))