import numpy as np 

def function(x):

	r5 = 2
	g4 = x
	paths = []
	try:
		if g4 <= 6:
			g4 = g4*9
			paths.append(1)
		else:
			x = 0+x
			x = 5+5
			paths.append(2)
		if g4 >= 0:
			g4 = g4-5
			g4 = g4/4
			g4 = 3-9
			paths.append(3)
		else:
			r5 = 6/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))