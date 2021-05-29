import numpy as np 

def function(x):

	y6 = x
	o0 = 4
	paths = []
	try:
		if x >= 0:
			y6 = x/y6
			x = 2+x
			paths.append(1)
		else:
			x = x-7
			x = 6-y6
			x = x+6
			paths.append(2)
		if y6 >= 1:
			o0 = o0-x
			y6 = y6+o0
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		y6 = o0**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))