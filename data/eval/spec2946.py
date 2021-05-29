import numpy as np 

def function(x):

	d1 = 2
	d8 = x
	paths = []
	try:
		if d1 < 7:
			d1 = d8+x
			x = 6/x
			paths.append(1)
		else:
			x = 3/7
			x = 8+x
			d8 = 4*x
			paths.append(2)
		if d1 > 9:
			d8 = 1*d8
			x = x+8
			paths.append(3)
		else:
			d1 = d1+4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d1 = d8**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))