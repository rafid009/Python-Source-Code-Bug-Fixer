import numpy as np 

def function(x):

	l7 = 2
	u5 = 3
	paths = []
	try:
		if x < 0:
			l7 = l7+u5
			u5 = u5*5
			paths.append(1)
		else:
			l7 = l7/9
			l7 = 9+l7
			u5 = u5/8
			paths.append(2)
		if x >= 9:
			l7 = 8/l7
			paths.append(3)
		else:
			u5 = x/8
			x = x-4
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