import numpy as np 

def function(x):

	g4 = 1
	t9 = 7
	paths = []
	try:
		if x >= 5:
			t9 = 3/t9
			g4 = t9*7
			paths.append(1)
		else:
			x = 1-x
			g4 = g4-9
			g4 = 7+4
			paths.append(2)
		if t9 > 5:
			x = x-g4
			paths.append(3)
		else:
			x = 6-x
			g4 = t9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))