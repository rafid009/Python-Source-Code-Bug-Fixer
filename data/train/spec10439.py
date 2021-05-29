import numpy as np 

def function(x):

	g4 = 2
	t0 = 8
	paths = []
	try:
		if g4 >= 1:
			t0 = x-6
			paths.append(1)
		else:
			g4 = g4-g4
			x = x/g4
			paths.append(2)
		if g4 >= 0:
			x = x/5
			g4 = g4/9
			g4 = g4-1
			paths.append(3)
		else:
			x = 7+4
			x = 3*t0
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		t0 = g4**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))