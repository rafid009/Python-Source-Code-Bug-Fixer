import numpy as np 

def function(x):

	b0 = 5
	y0 = x
	paths = []
	try:
		if y0 < 5:
			x = x/y0
			b0 = 4-b0
			b0 = x/9
			paths.append(1)
		else:
			x = 0+6
			y0 = 8-y0
			b0 = 7/2
			paths.append(2)
		if x >= 9:
			x = b0*4
			y0 = y0+y0
			b0 = 6*0
			paths.append(3)
		else:
			x = x*x
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