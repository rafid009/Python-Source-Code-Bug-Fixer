import numpy as np 

def function(x):

	j4 = 5
	g8 = 4
	paths = []
	try:
		if j4 >= 4:
			g8 = g8/6
			j4 = 4-8
			paths.append(1)
		else:
			g8 = g8-g8
			j4 = g8+1
			g8 = g8*3
			paths.append(2)
		if g8 <= 8:
			x = 1/x
			x = x-j4
			g8 = g8/x
			paths.append(3)
		else:
			g8 = g8-5
			j4 = j4+g8
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		g8 = j4**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))