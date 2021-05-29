import numpy as np 

def function(x):

	u4 = 5
	l5 = 0
	x = x
	paths = []
	try:
		if x <= 8:
			x = l5-x
			paths.append(1)
		else:
			l5 = 7*l5
			x = x-u4
			u4 = 3*u4
			paths.append(2)
		if u4 <= 0:
			u4 = 1*4
			paths.append(3)
		else:
			l5 = l5/u4
			u4 = 6/7
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