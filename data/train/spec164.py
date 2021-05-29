import numpy as np 

def function(x):

	l8 = x
	u6 = 8
	paths = []
	try:
		if l8 >= 5:
			u6 = 6*u6
			x = u6+l8
			paths.append(1)
		else:
			l8 = l8-x
			paths.append(2)
		if x >= 1:
			l8 = l8-3
			u6 = u6-9
			u6 = u6+5
			paths.append(3)
		else:
			l8 = 6-l8
			l8 = l8+8
			x = l8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))