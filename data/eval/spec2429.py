import numpy as np 

def function(x):

	y1 = x
	o3 = 8
	paths = []
	try:
		if x >= 3:
			y1 = y1*x
			paths.append(1)
		else:
			o3 = y1/o3
			paths.append(2)
		if y1 < 9:
			y1 = 8-5
			o3 = y1*o3
			o3 = 7/o3
			paths.append(3)
		else:
			x = x+x
			o3 = x+3
			x = x*4
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