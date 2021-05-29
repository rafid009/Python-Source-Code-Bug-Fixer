import numpy as np 

def function(x):

	y0 = x
	k6 = 0
	x = x
	paths = []
	try:
		if x >= 4:
			y0 = k6-y0
			x = x+x
			y0 = 2-y0
			paths.append(1)
		else:
			x = k6-x
			k6 = 9/9
			y0 = y0+1
			paths.append(2)
		if k6 > 4:
			x = x-3
			y0 = y0/y0
			k6 = 5/7
			paths.append(3)
		else:
			y0 = y0*x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))