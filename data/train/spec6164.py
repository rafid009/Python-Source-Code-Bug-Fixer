import numpy as np 

def function(x):

	r2 = 0
	d1 = x
	paths = []
	try:
		if x >= 1:
			d1 = d1-1
			paths.append(1)
		else:
			d1 = d1*4
			paths.append(2)
		if x <= 3:
			x = 6/x
			r2 = r2/1
			paths.append(3)
		else:
			r2 = 8*r2
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