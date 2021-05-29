import numpy as np 

def function(x):

	u2 = 2
	g0 = 6
	paths = []
	try:
		if x <= 3:
			u2 = x/7
			g0 = g0*0
			x = x/1
			paths.append(1)
		else:
			x = 4-8
			paths.append(2)
		if g0 < 4:
			g0 = 9-g0
			paths.append(3)
		else:
			g0 = g0+3
			g0 = g0*u2
			u2 = g0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))