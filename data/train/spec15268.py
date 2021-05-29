import numpy as np 

def function(x):

	d8 = x
	v5 = x
	paths = []
	try:
		if v5 >= 2:
			d8 = v5*7
			v5 = 7/v5
			paths.append(1)
		else:
			x = 8/5
			d8 = d8/x
			paths.append(2)
		if x >= 6:
			x = 3*x
			d8 = v5/v5
			paths.append(3)
		else:
			x = 9*d8
			x = 3*9
			v5 = v5*5
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