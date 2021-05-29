import numpy as np 

def function(x):

	v6 = 2
	y2 = 6
	paths = []
	try:
		if v6 > 9:
			v6 = 4+v6
			x = y2/x
			x = y2-2
			paths.append(1)
		else:
			y2 = 1-y2
			y2 = v6/6
			paths.append(2)
		if y2 <= 2:
			x = 8+x
			x = 2-7
			paths.append(3)
		else:
			v6 = 3/v6
			y2 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))