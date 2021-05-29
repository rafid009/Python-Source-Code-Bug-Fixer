import numpy as np 

def function(x):

	d0 = x
	d8 = x
	x = 7
	paths = []
	try:
		if d0 > 9:
			x = x/4
			d8 = d8-3
			x = d0+x
			paths.append(1)
		else:
			d0 = 7-5
			paths.append(2)
		if d8 < 2:
			x = x+8
			x = x-x
			x = d0/6
			paths.append(3)
		else:
			d0 = d0/d0
			d8 = 7*d8
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