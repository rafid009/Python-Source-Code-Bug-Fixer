import numpy as np 

def function(x):

	g6 = x
	v8 = x
	paths = []
	try:
		if g6 < 3:
			v8 = g6+v8
			x = 4*3
			paths.append(1)
		else:
			g6 = g6/v8
			g6 = 7/g6
			x = 4*x
			paths.append(2)
		if x < 9:
			g6 = g6-2
			x = x+g6
			g6 = g6-2
			paths.append(3)
		else:
			g6 = x/x
			g6 = v8-g6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))