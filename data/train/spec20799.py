import numpy as np 

def function(x):

	u4 = 2
	y3 = 7
	paths = []
	try:
		if y3 <= 8:
			u4 = 8+2
			x = 9-x
			paths.append(1)
		else:
			u4 = u4/4
			x = y3/x
			y3 = y3/u4
			paths.append(2)
		if y3 < 6:
			x = u4-y3
			y3 = u4+x
			y3 = x+x
			paths.append(3)
		else:
			y3 = u4+9
			u4 = u4-5
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