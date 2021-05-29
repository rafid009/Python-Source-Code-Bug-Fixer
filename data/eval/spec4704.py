import numpy as np 

def function(x):

	u2 = x
	g5 = x
	paths = []
	try:
		if u2 <= 2:
			x = x+2
			paths.append(1)
		else:
			x = x*u2
			paths.append(2)
		if g5 <= 2:
			g5 = g5/4
			g5 = g5+0
			x = 2+g5
			paths.append(3)
		else:
			u2 = 3+g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))