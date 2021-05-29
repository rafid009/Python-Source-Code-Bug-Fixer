import numpy as np 

def function(x):

	r6 = x
	g9 = 1
	x = 7
	paths = []
	try:
		if g9 <= 0:
			x = 4-x
			paths.append(1)
		else:
			x = 7/x
			g9 = g9*g9
			paths.append(2)
		if r6 < 8:
			g9 = 7+g9
			x = 4-2
			r6 = r6-x
			paths.append(3)
		else:
			x = r6-x
			x = x-3
			r6 = x/r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		g9 = r6**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))