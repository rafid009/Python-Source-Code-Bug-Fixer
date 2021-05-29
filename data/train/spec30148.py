import numpy as np 

def function(x):

	l4 = 0
	u4 = 8
	paths = []
	try:
		if l4 < 5:
			l4 = l4*6
			paths.append(1)
		else:
			u4 = u4-2
			paths.append(2)
		if l4 < 0:
			l4 = 8-7
			x = 7-6
			paths.append(3)
		else:
			l4 = l4+2
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