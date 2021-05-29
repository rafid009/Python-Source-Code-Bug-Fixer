import numpy as np 

def function(x):

	d7 = x
	d4 = 4
	x = 4
	paths = []
	try:
		if d7 < 6:
			d4 = d4/4
			paths.append(1)
		else:
			d4 = d4*5
			d7 = d7/6
			d7 = 3-8
			paths.append(2)
		if d7 <= 8:
			d7 = d4*9
			d4 = d4*9
			x = 2-x
			paths.append(3)
		else:
			x = 6-6
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