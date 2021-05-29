import numpy as np 

def function(x):

	u4 = x
	x8 = x
	paths = []
	try:
		if x8 > 8:
			u4 = u4/3
			paths.append(1)
		else:
			u4 = u4/6
			paths.append(2)
		if x8 >= 5:
			x = 8/1
			x8 = 4+x8
			u4 = x/4
			paths.append(3)
		else:
			x8 = u4+x8
			x8 = x8-2
			x = 8*5
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