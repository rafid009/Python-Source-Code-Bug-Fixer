import numpy as np 

def function(x):

	d6 = 6
	q8 = 2
	paths = []
	try:
		if x <= 0:
			q8 = 9/x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if q8 >= 5:
			q8 = q8+8
			paths.append(3)
		else:
			d6 = 6*x
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))