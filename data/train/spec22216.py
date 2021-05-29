import numpy as np 

def function(x):

	g0 = 0
	u2 = x
	paths = []
	try:
		if x >= 2:
			g0 = g0/4
			paths.append(1)
		else:
			x = x-6
			g0 = u2+9
			g0 = g0*g0
			paths.append(2)
		if x <= 7:
			u2 = 2-g0
			g0 = 6/4
			paths.append(3)
		else:
			g0 = 1*4
			x = x-4
			u2 = x-u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))