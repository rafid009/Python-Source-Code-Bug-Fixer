import numpy as np 

def function(x):

	d0 = 2
	d4 = x
	paths = []
	try:
		if x >= 9:
			x = x+6
			paths.append(1)
		else:
			d0 = 4+6
			paths.append(2)
		if x > 2:
			x = x/5
			x = d0/5
			paths.append(3)
		else:
			d0 = 4-d0
			d0 = d0-d4
			x = 2+7
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))