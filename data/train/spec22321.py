import numpy as np 

def function(x):

	v1 = x
	g3 = 0
	x = x
	paths = []
	try:
		if g3 < 5:
			v1 = 2+3
			v1 = v1*6
			g3 = x-g3
			paths.append(1)
		else:
			g3 = 8+g3
			g3 = 9*g3
			paths.append(2)
		if v1 > 9:
			g3 = 1/g3
			v1 = 1+v1
			paths.append(3)
		else:
			v1 = 7-g3
			x = 1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))