import numpy as np 

def function(x):

	r7 = x
	y1 = 6
	paths = []
	try:
		if x > 6:
			y1 = y1/y1
			y1 = y1/y1
			r7 = 6/r7
			paths.append(1)
		else:
			x = x*4
			x = x/5
			paths.append(2)
		if r7 >= 4:
			r7 = r7-3
			paths.append(3)
		else:
			r7 = r7/r7
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