import numpy as np 

def function(x):

	b5 = 7
	u4 = x
	x = x
	paths = []
	try:
		if x >= 9:
			b5 = 3/7
			x = 9+8
			paths.append(1)
		else:
			b5 = b5-u4
			x = b5/5
			paths.append(2)
		if x < 9:
			x = u4+5
			u4 = u4+6
			paths.append(3)
		else:
			u4 = 8-9
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))