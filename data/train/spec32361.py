import numpy as np 

def function(x):

	y2 = x
	o3 = x
	paths = []
	try:
		if x >= 2:
			o3 = 0-8
			x = x+1
			o3 = o3-x
			paths.append(1)
		else:
			y2 = 9/x
			o3 = 6*o3
			paths.append(2)
		if x <= 4:
			x = x-0
			x = x*o3
			y2 = y2+3
			paths.append(3)
		else:
			y2 = y2+5
			o3 = o3+o3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))