import numpy as np 

def function(x):

	b0 = 5
	d8 = x
	x = 0
	paths = []
	try:
		if d8 < 7:
			b0 = b0-4
			x = 1/d8
			b0 = d8-1
			paths.append(1)
		else:
			b0 = 5+b0
			b0 = d8-x
			paths.append(2)
		if x > 3:
			d8 = 4*d8
			x = 0+b0
			paths.append(3)
		else:
			x = x*4
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