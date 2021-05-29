import numpy as np 

def function(x):

	g4 = 7
	r6 = 8
	paths = []
	try:
		if x > 8:
			x = 4+x
			g4 = g4-0
			paths.append(1)
		else:
			x = x-r6
			g4 = 0-9
			g4 = g4+4
			paths.append(2)
		if g4 <= 8:
			r6 = g4+6
			r6 = 4*x
			paths.append(3)
		else:
			g4 = 9/2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		g4 = r6**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))