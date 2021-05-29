import numpy as np 

def function(x):

	u7 = x
	g5 = x
	paths = []
	try:
		if u7 > 8:
			x = x/2
			g5 = g5-2
			u7 = x*u7
			paths.append(1)
		else:
			u7 = 9-4
			paths.append(2)
		if x <= 2:
			u7 = x/u7
			g5 = 5+u7
			x = 7+x
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))