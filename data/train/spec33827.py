import numpy as np 

def function(x):

	b1 = x
	y0 = x
	paths = []
	try:
		if x < 6:
			x = b1+b1
			x = 1+4
			paths.append(1)
		else:
			y0 = y0-6
			x = x+9
			x = 7*x
			paths.append(2)
		if y0 < 7:
			x = x-y0
			y0 = y0*2
			paths.append(3)
		else:
			y0 = 0+8
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))