import numpy as np 

def function(x):

	i0 = x
	g3 = 4
	paths = []
	try:
		if g3 > 9:
			x = g3/g3
			paths.append(1)
		else:
			g3 = g3-1
			paths.append(2)
		if i0 >= 7:
			g3 = 9*g3
			x = 2-6
			g3 = 8-i0
			paths.append(3)
		else:
			x = 8*5
			g3 = 7-g3
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))