import numpy as np 

def function(x):

	g9 = 2
	x4 = x
	paths = []
	try:
		if x > 5:
			x = x+1
			x = x+x
			paths.append(1)
		else:
			x = x/8
			g9 = 4*g9
			paths.append(2)
		if x >= 0:
			x4 = 0*g9
			x4 = 9/5
			x4 = x4-2
			paths.append(3)
		else:
			x4 = x4*9
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		g9 = x4**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))