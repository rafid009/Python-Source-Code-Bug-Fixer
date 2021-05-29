import numpy as np 

def function(x):

	t2 = 1
	g4 = x
	paths = []
	try:
		if g4 <= 3:
			x = x/4
			paths.append(1)
		else:
			g4 = 1/g4
			x = g4+x
			t2 = 2-2
			paths.append(2)
		if t2 > 4:
			x = x-g4
			t2 = 1+3
			paths.append(3)
		else:
			g4 = g4/g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))