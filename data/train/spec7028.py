import numpy as np 

def function(x):

	y5 = 3
	d5 = x
	paths = []
	try:
		if y5 > 0:
			x = x+4
			y5 = x/2
			y5 = y5/y5
			paths.append(1)
		else:
			y5 = 7/x
			x = x-3
			x = 0*3
			paths.append(2)
		if y5 >= 0:
			y5 = x*x
			y5 = y5+1
			x = x*d5
			paths.append(3)
		else:
			d5 = d5-7
			y5 = y5-3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))