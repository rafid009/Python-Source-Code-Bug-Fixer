import numpy as np 

def function(x):

	b0 = x
	y0 = x
	paths = []
	try:
		if x > 5:
			b0 = b0+7
			paths.append(1)
		else:
			y0 = x/b0
			b0 = 6*9
			b0 = y0-b0
			paths.append(2)
		if y0 > 8:
			x = b0*9
			y0 = y0*5
			x = x/9
			paths.append(3)
		else:
			x = 7-x
			y0 = 1+y0
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		y0 = b0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))