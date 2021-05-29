import numpy as np 

def function(x):

	y0 = 9
	i9 = 0
	paths = []
	try:
		if y0 < 7:
			y0 = y0-5
			paths.append(1)
		else:
			y0 = 1-y0
			i9 = 5-i9
			i9 = y0+i9
			paths.append(2)
		if i9 >= 7:
			x = x*8
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		i9 = y0**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))