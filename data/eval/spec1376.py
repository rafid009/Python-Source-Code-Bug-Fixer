import numpy as np 

def function(x):

	y0 = 2
	d4 = x
	paths = []
	try:
		if d4 <= 4:
			x = x+3
			paths.append(1)
		else:
			d4 = d4-5
			x = x+x
			x = y0*4
			paths.append(2)
		if d4 > 7:
			d4 = d4+3
			y0 = y0+6
			paths.append(3)
		else:
			x = x/d4
			y0 = y0*4
			y0 = 6-y0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))