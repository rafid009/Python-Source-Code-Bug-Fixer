import numpy as np 

def function(x):

	u4 = 2
	g0 = 7
	paths = []
	try:
		if u4 <= 3:
			x = g0/x
			paths.append(1)
		else:
			g0 = x+g0
			u4 = 6+u4
			paths.append(2)
		if u4 < 6:
			u4 = 2+2
			paths.append(3)
		else:
			u4 = u4/5
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