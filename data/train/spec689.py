import numpy as np 

def function(x):

	q8 = x
	d4 = x
	paths = []
	try:
		if x < 4:
			d4 = d4-x
			q8 = q8*7
			q8 = q8+9
			paths.append(1)
		else:
			x = x*9
			q8 = 9+7
			d4 = d4*q8
			paths.append(2)
		if q8 <= 6:
			d4 = d4*7
			d4 = 6/4
			paths.append(3)
		else:
			x = x-6
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))