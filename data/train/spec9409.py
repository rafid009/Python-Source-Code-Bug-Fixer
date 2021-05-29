import numpy as np 

def function(x):

	y0 = 0
	i6 = 3
	paths = []
	try:
		if x < 4:
			y0 = y0-0
			x = 8+4
			paths.append(1)
		else:
			i6 = i6*8
			i6 = 0-i6
			paths.append(2)
		if i6 < 2:
			x = x-x
			paths.append(3)
		else:
			x = i6+4
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))