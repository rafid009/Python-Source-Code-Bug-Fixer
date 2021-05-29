import numpy as np 

def function(x):

	q8 = x
	d6 = 2
	paths = []
	try:
		if x >= 3:
			q8 = 8-q8
			paths.append(1)
		else:
			x = d6*x
			paths.append(2)
		if q8 >= 7:
			q8 = q8*1
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))