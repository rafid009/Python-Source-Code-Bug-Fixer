import numpy as np 

def function(x):

	f9 = 8
	d8 = x
	paths = []
	try:
		if x < 1:
			x = f9/x
			d8 = 7/d8
			paths.append(1)
		else:
			f9 = 2-x
			paths.append(2)
		if d8 > 0:
			d8 = 1*d8
			paths.append(3)
		else:
			d8 = x+d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))