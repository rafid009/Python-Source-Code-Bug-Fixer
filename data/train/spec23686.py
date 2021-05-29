import numpy as np 

def function(x):

	r8 = x
	g7 = 7
	paths = []
	try:
		if g7 >= 8:
			x = 4*9
			x = 1-2
			g7 = 4/g7
			paths.append(1)
		else:
			r8 = 4*r8
			g7 = x+1
			paths.append(2)
		if g7 <= 2:
			r8 = r8/1
			x = x-r8
			g7 = g7/4
			paths.append(3)
		else:
			g7 = g7-1
			x = x+r8
			x = 5-5
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		g7 = r8**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))