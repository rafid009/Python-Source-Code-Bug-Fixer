import numpy as np 

def function(x):

	d0 = 8
	u4 = 1
	paths = []
	try:
		if u4 > 7:
			u4 = u4*u4
			u4 = u4*6
			u4 = 6/u4
			paths.append(1)
		else:
			x = 7*x
			u4 = u4*8
			paths.append(2)
		if d0 > 8:
			x = x+5
			paths.append(3)
		else:
			x = 1-6
			d0 = d0-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))