import numpy as np 

def function(x):

	g9 = 4
	q0 = 5
	paths = []
	try:
		if x < 9:
			g9 = x*g9
			q0 = g9-q0
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if g9 < 3:
			g9 = g9+8
			g9 = g9-x
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		g9 = q0**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))