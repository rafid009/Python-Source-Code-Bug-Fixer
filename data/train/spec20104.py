import numpy as np 

def function(x):

	g8 = 8
	l3 = 8
	paths = []
	try:
		if g8 >= 6:
			g8 = 1-g8
			paths.append(1)
		else:
			g8 = 7+0
			g8 = g8/9
			paths.append(2)
		if x > 5:
			x = 7+x
			x = x+g8
			l3 = l3*g8
			paths.append(3)
		else:
			x = x/6
			g8 = l3-g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))