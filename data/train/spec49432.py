import numpy as np 

def function(x):

	y1 = x
	o3 = 2
	paths = []
	try:
		if o3 <= 0:
			o3 = o3+0
			y1 = 9+y1
			paths.append(1)
		else:
			x = 3*x
			x = x*9
			o3 = y1/o3
			paths.append(2)
		if o3 >= 4:
			x = x+o3
			y1 = x*y1
			paths.append(3)
		else:
			o3 = o3/y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))