import numpy as np 

def function(x):

	g6 = x
	d0 = 6
	paths = []
	try:
		if g6 <= 6:
			g6 = x*1
			paths.append(1)
		else:
			d0 = d0+9
			paths.append(2)
		if d0 < 6:
			x = 3/x
			g6 = g6+0
			d0 = x+x
			paths.append(3)
		else:
			d0 = 8+8
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))