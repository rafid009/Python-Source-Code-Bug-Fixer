import numpy as np 

def function(x):

	y8 = x
	w5 = x
	paths = []
	try:
		if w5 >= 3:
			y8 = 4+y8
			y8 = 4*y8
			paths.append(1)
		else:
			y8 = y8+6
			paths.append(2)
		if w5 >= 7:
			x = x-4
			w5 = w5-3
			paths.append(3)
		else:
			w5 = w5*y8
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