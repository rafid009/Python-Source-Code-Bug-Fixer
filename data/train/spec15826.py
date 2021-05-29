import numpy as np 

def function(x):

	g1 = x
	o3 = x
	paths = []
	try:
		if g1 > 7:
			o3 = o3/3
			g1 = 4*g1
			o3 = 3+o3
			paths.append(1)
		else:
			g1 = 6/g1
			paths.append(2)
		if g1 <= 0:
			x = 8+o3
			o3 = o3*8
			paths.append(3)
		else:
			x = g1*x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		g1 = o3**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))