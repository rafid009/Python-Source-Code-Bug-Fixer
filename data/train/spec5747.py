import numpy as np 

def function(x):

	r0 = 8
	g4 = x
	paths = []
	try:
		if r0 > 8:
			r0 = r0-9
			r0 = 7+1
			paths.append(1)
		else:
			r0 = 2+7
			x = 2+x
			r0 = g4/r0
			paths.append(2)
		if x >= 9:
			g4 = g4*5
			paths.append(3)
		else:
			g4 = 0*1
			x = x+3
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