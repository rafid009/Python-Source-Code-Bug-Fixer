import numpy as np 

def function(x):

	y3 = x
	d0 = 3
	paths = []
	try:
		if x < 7:
			x = 6*7
			x = 2+x
			y3 = y3*1
			paths.append(1)
		else:
			d0 = d0+6
			x = 6-x
			paths.append(2)
		if x > 8:
			d0 = x*d0
			d0 = 8-d0
			x = d0+x
			paths.append(3)
		else:
			d0 = d0/y3
			y3 = 8-y3
			y3 = 8*5
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