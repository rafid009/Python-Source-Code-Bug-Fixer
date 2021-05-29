import numpy as np 

def function(x):

	q8 = x
	d1 = 6
	paths = []
	try:
		if d1 <= 9:
			d1 = d1*q8
			paths.append(1)
		else:
			q8 = q8-4
			paths.append(2)
		if d1 > 0:
			x = x-5
			q8 = q8+2
			paths.append(3)
		else:
			x = d1-d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))