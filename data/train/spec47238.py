import numpy as np 

def function(x):

	g0 = x
	f2 = x
	paths = []
	try:
		if x > 6:
			g0 = 1+2
			paths.append(1)
		else:
			x = x*x
			f2 = x+8
			g0 = 6*g0
			paths.append(2)
		if f2 < 8:
			f2 = 4+8
			x = x-8
			paths.append(3)
		else:
			f2 = 0/x
			g0 = g0-4
			f2 = g0+2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))