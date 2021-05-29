import numpy as np 

def function(x):

	y0 = 5
	d8 = 4
	paths = []
	try:
		if d8 > 4:
			x = 9+x
			x = 2-9
			y0 = 8*1
			paths.append(1)
		else:
			d8 = d8+x
			y0 = 1+y0
			paths.append(2)
		if x > 2:
			y0 = y0*4
			x = x*8
			x = x*0
			paths.append(3)
		else:
			x = x-y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))