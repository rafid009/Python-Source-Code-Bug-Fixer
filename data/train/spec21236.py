import numpy as np 

def function(x):

	y8 = 7
	v4 = x
	x = x
	paths = []
	try:
		if y8 < 2:
			x = v4+9
			y8 = v4/y8
			paths.append(1)
		else:
			v4 = y8*v4
			paths.append(2)
		if x >= 0:
			y8 = 7-7
			v4 = y8*v4
			y8 = 9+y8
			paths.append(3)
		else:
			v4 = v4-x
			y8 = 3+6
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))