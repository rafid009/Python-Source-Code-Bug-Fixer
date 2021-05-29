import numpy as np 

def function(x):

	i1 = x
	g6 = x
	paths = []
	try:
		if i1 > 6:
			g6 = 9+9
			g6 = g6/g6
			x = x*8
			paths.append(1)
		else:
			g6 = g6+i1
			g6 = g6-6
			paths.append(2)
		if g6 > 9:
			x = x+2
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))