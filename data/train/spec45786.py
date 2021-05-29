import numpy as np 

def function(x):

	d0 = 5
	y3 = x
	paths = []
	try:
		if d0 <= 5:
			x = x+6
			d0 = d0/y3
			paths.append(1)
		else:
			y3 = y3-8
			x = x+x
			y3 = d0/3
			paths.append(2)
		if y3 >= 9:
			y3 = x+0
			paths.append(3)
		else:
			d0 = 0+d0
			y3 = y3*3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))