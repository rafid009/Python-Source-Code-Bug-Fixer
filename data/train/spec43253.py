import numpy as np 

def function(x):

	q6 = 2
	d4 = 8
	paths = []
	try:
		if q6 < 1:
			d4 = x-0
			paths.append(1)
		else:
			q6 = q6-8
			q6 = q6*x
			d4 = 4+d4
			paths.append(2)
		if q6 >= 4:
			x = x-7
			d4 = 3-d4
			x = 0+d4
			paths.append(3)
		else:
			q6 = d4*9
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))