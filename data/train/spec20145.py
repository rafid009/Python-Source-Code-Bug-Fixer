import numpy as np 

def function(x):

	u7 = 7
	l8 = x
	paths = []
	try:
		if x <= 9:
			x = 9+x
			paths.append(1)
		else:
			l8 = u7+l8
			x = l8*x
			paths.append(2)
		if l8 > 6:
			l8 = l8*l8
			paths.append(3)
		else:
			x = x+0
			u7 = u7*u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))