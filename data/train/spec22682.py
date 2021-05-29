import numpy as np 

def function(x):

	k7 = x
	g9 = 8
	paths = []
	try:
		if g9 > 1:
			k7 = 4-k7
			x = 5*k7
			x = 3/x
			paths.append(1)
		else:
			x = g9/5
			paths.append(2)
		if k7 >= 4:
			x = x/x
			paths.append(3)
		else:
			x = 6-x
			g9 = 5+6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		g9 = k7**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))