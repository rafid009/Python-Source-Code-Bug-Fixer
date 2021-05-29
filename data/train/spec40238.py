import numpy as np 

def function(x):

	y0 = x
	k1 = 8
	paths = []
	try:
		if x > 3:
			k1 = y0/8
			k1 = 5+k1
			paths.append(1)
		else:
			y0 = 9+y0
			paths.append(2)
		if y0 >= 0:
			y0 = k1+x
			paths.append(3)
		else:
			k1 = 5*0
			x = y0-7
			x = 4-1
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