import numpy as np 

def function(x):

	q8 = x
	n6 = x
	paths = []
	try:
		if q8 <= 5:
			n6 = q8+n6
			paths.append(1)
		else:
			q8 = q8*6
			q8 = q8*n6
			q8 = q8-n6
			paths.append(2)
		if q8 >= 7:
			x = 8+9
			x = 4-x
			n6 = n6/1
			paths.append(3)
		else:
			x = 4*x
			n6 = 2*n6
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))