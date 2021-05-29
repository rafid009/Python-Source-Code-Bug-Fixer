import numpy as np 

def function(x):

	g3 = x
	k7 = x
	paths = []
	try:
		if x >= 4:
			k7 = k7/x
			k7 = g3*2
			x = x+x
			paths.append(1)
		else:
			g3 = 5*g3
			paths.append(2)
		if x >= 9:
			k7 = 6*g3
			x = x-5
			paths.append(3)
		else:
			k7 = 6*k7
			g3 = g3-6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		g3 = k7**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))