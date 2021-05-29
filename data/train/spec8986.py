import numpy as np 

def function(x):

	t4 = 5
	g1 = 1
	paths = []
	try:
		if t4 > 2:
			t4 = 8*g1
			g1 = t4+t4
			g1 = 4+7
			paths.append(1)
		else:
			t4 = 4+t4
			x = t4*2
			t4 = t4-g1
			paths.append(2)
		if x < 3:
			g1 = 9+7
			x = 1/x
			g1 = g1/3
			paths.append(3)
		else:
			t4 = t4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))