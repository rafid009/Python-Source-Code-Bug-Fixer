import numpy as np 

def function(x):

	t0 = 4
	g4 = x
	x = x
	paths = []
	try:
		if t0 > 3:
			t0 = t0-1
			paths.append(1)
		else:
			t0 = t0/4
			g4 = g4+9
			g4 = g4/1
			paths.append(2)
		if x >= 2:
			x = 7+4
			paths.append(3)
		else:
			g4 = x+g4
			t0 = t0-5
			t0 = 3/t0
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))