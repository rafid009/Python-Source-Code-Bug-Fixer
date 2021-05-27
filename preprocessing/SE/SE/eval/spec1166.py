import numpy as np 

def function(x):

	g5 = 2
	b6 = x
	paths = []
	try:
		if g5 > 7:
			g5 = g5+8
			b6 = 7*b6
			x = x*b6
			paths.append(1)
		else:
			x = x+2
			x = x/8
			b6 = x/b6
			paths.append(2)
		if g5 >= 5:
			x = 8/x
			g5 = g5/6
			paths.append(3)
		else:
			g5 = g5*5
			g5 = 6+g5
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		g5 = b6**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))