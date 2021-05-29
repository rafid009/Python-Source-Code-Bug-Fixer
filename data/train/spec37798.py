import numpy as np 

def function(x):

	v3 = x
	y7 = x
	paths = []
	try:
		if v3 > 2:
			v3 = 3-3
			x = 4*6
			paths.append(1)
		else:
			v3 = v3+2
			x = y7*3
			paths.append(2)
		if y7 < 4:
			x = x/7
			paths.append(3)
		else:
			x = y7-3
			v3 = 9+4
			y7 = 2-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))