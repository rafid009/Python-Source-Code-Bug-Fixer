import numpy as np 

def function(x):

	v6 = x
	g4 = x
	paths = []
	try:
		if x < 6:
			v6 = 4+v6
			paths.append(1)
		else:
			x = 8-g4
			g4 = x*g4
			paths.append(2)
		if v6 <= 0:
			x = v6+7
			g4 = 9/8
			paths.append(3)
		else:
			x = 0-5
			x = x/6
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