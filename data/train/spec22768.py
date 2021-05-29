import numpy as np 

def function(x):

	y1 = x
	k1 = 7
	paths = []
	try:
		if k1 > 3:
			y1 = y1-8
			paths.append(1)
		else:
			y1 = y1-7
			k1 = x*1
			y1 = 8/y1
			paths.append(2)
		if k1 >= 6:
			x = 5-x
			x = 1+x
			paths.append(3)
		else:
			x = k1/6
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))