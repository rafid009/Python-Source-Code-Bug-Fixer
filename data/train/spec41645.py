import numpy as np 

def function(x):

	x6 = 7
	g5 = 9
	paths = []
	try:
		if g5 < 7:
			g5 = g5-6
			paths.append(1)
		else:
			x = x+3
			g5 = g5-8
			paths.append(2)
		if g5 >= 8:
			x = x*3
			g5 = 9+g5
			paths.append(3)
		else:
			x6 = x+g5
			x = x+1
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		g5 = x6**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))