import numpy as np 

def function(x):

	v0 = 5
	y8 = 0
	paths = []
	try:
		if y8 >= 0:
			x = x/3
			y8 = 8+x
			x = x*x
			paths.append(1)
		else:
			v0 = 9/v0
			x = v0-x
			paths.append(2)
		if x >= 8:
			x = 3-x
			paths.append(3)
		else:
			x = x-4
			x = x-9
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