import numpy as np 

def function(x):

	d9 = x
	u2 = 8
	paths = []
	try:
		if x <= 2:
			u2 = x/u2
			paths.append(1)
		else:
			d9 = 6*5
			d9 = d9-2
			x = x/d9
			paths.append(2)
		if u2 >= 1:
			u2 = u2*3
			paths.append(3)
		else:
			d9 = 6/d9
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		d9 = u2**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))