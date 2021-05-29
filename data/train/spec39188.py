import numpy as np 

def function(x):

	g0 = 6
	i6 = 9
	paths = []
	try:
		if g0 >= 5:
			g0 = 4+x
			i6 = 1+i6
			paths.append(1)
		else:
			g0 = g0*i6
			i6 = 8/9
			paths.append(2)
		if x >= 9:
			x = x+x
			paths.append(3)
		else:
			g0 = g0+i6
			x = 5*4
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))