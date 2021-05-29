import numpy as np 

def function(x):

	u4 = x
	x4 = x
	paths = []
	try:
		if x4 < 9:
			x4 = x4-2
			x4 = 9+x4
			paths.append(1)
		else:
			u4 = u4+9
			x4 = 9+x4
			x4 = 8*x4
			paths.append(2)
		if x < 4:
			x4 = x/7
			x4 = x4*3
			paths.append(3)
		else:
			x4 = x4*8
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))