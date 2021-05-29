import numpy as np 

def function(x):

	f9 = x
	y0 = 8
	paths = []
	try:
		if f9 > 1:
			f9 = y0+f9
			x = x*8
			paths.append(1)
		else:
			x = 6/x
			y0 = f9+8
			x = x/6
			paths.append(2)
		if y0 < 7:
			f9 = f9-6
			paths.append(3)
		else:
			x = y0*3
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))