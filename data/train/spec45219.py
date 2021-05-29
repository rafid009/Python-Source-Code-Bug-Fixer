import numpy as np 

def function(x):

	g3 = x
	x4 = x
	paths = []
	try:
		if g3 < 7:
			g3 = g3/x
			paths.append(1)
		else:
			x4 = g3*4
			paths.append(2)
		if x4 < 2:
			x = x/1
			x = 0+x
			x = x/x
			paths.append(3)
		else:
			x = g3/x
			x4 = g3*x4
			g3 = 8/g3
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))