import numpy as np 

def function(x):

	t6 = x
	g1 = 9
	paths = []
	try:
		if t6 < 5:
			x = x-5
			g1 = g1*7
			paths.append(1)
		else:
			t6 = 3*8
			t6 = t6*3
			paths.append(2)
		if t6 <= 3:
			x = x-1
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))