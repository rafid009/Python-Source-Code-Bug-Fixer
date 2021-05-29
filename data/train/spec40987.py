import numpy as np 

def function(x):

	w8 = 6
	y7 = 2
	paths = []
	try:
		if x < 9:
			w8 = w8/2
			x = 4+x
			w8 = 0-6
			paths.append(1)
		else:
			w8 = y7+w8
			w8 = 6+9
			paths.append(2)
		if y7 > 7:
			w8 = w8-6
			x = w8+8
			paths.append(3)
		else:
			x = 7/w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))