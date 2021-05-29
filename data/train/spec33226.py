import numpy as np 

def function(x):

	v7 = 2
	g3 = 1
	paths = []
	try:
		if g3 >= 5:
			x = v7-4
			g3 = 4-g3
			paths.append(1)
		else:
			g3 = 2-g3
			g3 = 0-g3
			x = 7*x
			paths.append(2)
		if g3 > 6:
			v7 = x*0
			v7 = v7/8
			paths.append(3)
		else:
			x = 8+x
			x = x/1
			g3 = 4-5
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