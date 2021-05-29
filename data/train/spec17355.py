import numpy as np 

def function(x):

	y0 = 7
	v3 = 7
	paths = []
	try:
		if v3 <= 0:
			x = 5*6
			y0 = y0-9
			x = 9-x
			paths.append(1)
		else:
			y0 = 4-y0
			v3 = 0+x
			paths.append(2)
		if x <= 6:
			v3 = v3/3
			paths.append(3)
		else:
			y0 = y0-3
			y0 = y0+7
			v3 = v3+3
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		v3 = y0**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))