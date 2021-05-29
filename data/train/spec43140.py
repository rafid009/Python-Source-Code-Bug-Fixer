import numpy as np 

def function(x):

	g7 = 5
	r8 = x
	paths = []
	try:
		if x >= 6:
			g7 = g7*4
			r8 = r8/4
			x = x-g7
			paths.append(1)
		else:
			r8 = 5+r8
			r8 = g7+r8
			g7 = g7-0
			paths.append(2)
		if x >= 6:
			g7 = 7/g7
			r8 = r8*5
			x = 6*x
			paths.append(3)
		else:
			r8 = 9*r8
			g7 = g7*g7
			g7 = 9-9
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))