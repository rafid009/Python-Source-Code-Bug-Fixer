import numpy as np 

def function(x):

	g4 = 6
	u5 = x
	paths = []
	try:
		if u5 >= 4:
			x = x*u5
			x = x+2
			g4 = 8-3
			paths.append(1)
		else:
			g4 = 8-g4
			g4 = u5+7
			paths.append(2)
		if g4 < 2:
			g4 = 6*u5
			u5 = 5+u5
			paths.append(3)
		else:
			g4 = 0*g4
			u5 = 9-u5
			g4 = g4/u5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))