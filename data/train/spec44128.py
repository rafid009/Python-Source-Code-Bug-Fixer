import numpy as np 

def function(x):

	i8 = x
	g1 = x
	x = 3
	paths = []
	try:
		if g1 >= 9:
			x = 4-x
			i8 = i8*5
			x = i8/4
			paths.append(1)
		else:
			g1 = 3+g1
			g1 = i8*g1
			paths.append(2)
		if i8 >= 9:
			x = g1/7
			g1 = 7/7
			paths.append(3)
		else:
			g1 = g1*5
			i8 = i8-0
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		g1 = i8**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))