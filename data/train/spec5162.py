import numpy as np 

def function(x):

	u4 = 9
	l5 = 6
	paths = []
	try:
		if u4 > 8:
			x = x/u4
			paths.append(1)
		else:
			u4 = 6*l5
			x = 4+x
			l5 = l5+x
			paths.append(2)
		if u4 > 6:
			u4 = x/x
			paths.append(3)
		else:
			u4 = u4+8
			u4 = 7-u4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))