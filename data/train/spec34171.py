import numpy as np 

def function(x):

	y6 = 5
	i0 = x
	paths = []
	try:
		if i0 < 0:
			x = 6/y6
			x = x+7
			y6 = i0+8
			paths.append(1)
		else:
			y6 = y6-8
			paths.append(2)
		if y6 <= 4:
			x = x-6
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		y6 = i0**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))