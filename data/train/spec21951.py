import numpy as np 

def function(x):

	g6 = x
	t1 = 3
	paths = []
	try:
		if x >= 6:
			t1 = x-6
			paths.append(1)
		else:
			g6 = x-t1
			x = x/x
			paths.append(2)
		if g6 < 9:
			t1 = 4-g6
			g6 = 2/g6
			paths.append(3)
		else:
			g6 = 0+g6
			t1 = t1*2
			g6 = g6-g6
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