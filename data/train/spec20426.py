import numpy as np 

def function(x):

	t7 = 0
	g4 = 8
	paths = []
	try:
		if t7 <= 6:
			t7 = 7*x
			g4 = g4-t7
			paths.append(1)
		else:
			x = x-x
			g4 = g4/x
			paths.append(2)
		if g4 >= 8:
			t7 = t7-1
			t7 = 7+4
			paths.append(3)
		else:
			g4 = 1-3
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