import numpy as np 

def function(x):

	g6 = x
	t4 = 3
	paths = []
	try:
		if g6 < 2:
			t4 = 0*9
			t4 = g6*3
			paths.append(1)
		else:
			x = x-3
			g6 = 3-x
			x = 8/8
			paths.append(2)
		if x > 3:
			x = x+9
			g6 = 7-3
			t4 = 4*g6
			paths.append(3)
		else:
			x = x-5
			g6 = 0/1
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))