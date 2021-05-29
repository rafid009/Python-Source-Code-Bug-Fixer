import numpy as np 

def function(x):

	g0 = 5
	u2 = x
	paths = []
	try:
		if u2 > 6:
			x = g0+7
			u2 = 2+x
			paths.append(1)
		else:
			u2 = g0/4
			g0 = g0*9
			paths.append(2)
		if g0 >= 1:
			x = g0/x
			x = 5+2
			x = 3-9
			paths.append(3)
		else:
			g0 = u2*g0
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