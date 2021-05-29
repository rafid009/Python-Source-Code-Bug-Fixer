import numpy as np 

def function(x):

	r9 = x
	g9 = 6
	paths = []
	try:
		if x < 5:
			x = 2/x
			paths.append(1)
		else:
			x = 1-g9
			x = 6-0
			r9 = 9*g9
			paths.append(2)
		if r9 <= 8:
			g9 = 4*r9
			g9 = g9+1
			paths.append(3)
		else:
			g9 = 8*g9
			x = g9/2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		g9 = r9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))