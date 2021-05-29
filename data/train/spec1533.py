import numpy as np 

def function(x):

	y8 = 6
	v0 = 3
	paths = []
	try:
		if y8 >= 1:
			y8 = y8*y8
			y8 = 6*x
			paths.append(1)
		else:
			y8 = 1/1
			v0 = x/v0
			y8 = y8-9
			paths.append(2)
		if x < 8:
			x = x-3
			v0 = 2/v0
			paths.append(3)
		else:
			x = 1*x
			y8 = 6+y8
			x = x+v0
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))