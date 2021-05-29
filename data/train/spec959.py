import numpy as np 

def function(x):

	y8 = x
	u4 = x
	paths = []
	try:
		if u4 >= 4:
			u4 = u4+2
			u4 = 5-u4
			u4 = 1/u4
			paths.append(1)
		else:
			u4 = u4-x
			y8 = 1-y8
			u4 = u4*2
			paths.append(2)
		if x > 8:
			x = y8/5
			x = x/8
			paths.append(3)
		else:
			y8 = 7+u4
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