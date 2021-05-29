import numpy as np 

def function(x):

	v9 = x
	d7 = 6
	paths = []
	try:
		if x > 1:
			d7 = 4-v9
			v9 = v9-7
			v9 = 6/v9
			paths.append(1)
		else:
			x = x-7
			d7 = v9+1
			paths.append(2)
		if v9 > 3:
			x = x-6
			paths.append(3)
		else:
			v9 = v9*6
			d7 = 4*d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))