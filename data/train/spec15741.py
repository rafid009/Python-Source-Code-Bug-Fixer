import numpy as np 

def function(x):

	y0 = x
	x8 = x
	x = 0
	paths = []
	try:
		if x >= 0:
			x = 0-2
			paths.append(1)
		else:
			x8 = y0*9
			x = x/6
			x = x8+x8
			paths.append(2)
		if x8 >= 4:
			x8 = y0*0
			x8 = x8+9
			x = x*2
			paths.append(3)
		else:
			y0 = y0*4
			x8 = 0/y0
			x8 = 4*x8
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x8 = y0**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))