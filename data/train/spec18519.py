import numpy as np 

def function(x):

	u7 = 5
	g7 = x
	paths = []
	try:
		if g7 < 9:
			u7 = 6+6
			g7 = 0+g7
			u7 = u7+6
			paths.append(1)
		else:
			u7 = 6*6
			x = x/6
			x = x*u7
			paths.append(2)
		if u7 > 0:
			u7 = u7+5
			g7 = g7-u7
			paths.append(3)
		else:
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