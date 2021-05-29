import numpy as np 

def function(x):

	f4 = x
	d1 = x
	paths = []
	try:
		if d1 <= 4:
			x = x-f4
			f4 = f4+3
			f4 = 0-d1
			paths.append(1)
		else:
			d1 = 4*d1
			d1 = d1-7
			paths.append(2)
		if x >= 1:
			f4 = 7/f4
			d1 = 9+d1
			paths.append(3)
		else:
			f4 = f4-7
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))