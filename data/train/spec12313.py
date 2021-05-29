import numpy as np 

def function(x):

	g8 = 1
	u4 = x
	paths = []
	try:
		if g8 >= 0:
			x = x+2
			x = g8-x
			paths.append(1)
		else:
			u4 = u4/7
			u4 = u4-g8
			paths.append(2)
		if u4 > 3:
			x = x+x
			x = g8-u4
			paths.append(3)
		else:
			x = u4-x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))