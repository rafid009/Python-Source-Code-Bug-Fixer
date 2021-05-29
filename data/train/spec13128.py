import numpy as np 

def function(x):

	g8 = 0
	q6 = x
	paths = []
	try:
		if q6 <= 4:
			g8 = g8+g8
			g8 = 5*g8
			g8 = g8*8
			paths.append(1)
		else:
			x = 4*7
			x = 5/x
			paths.append(2)
		if x <= 1:
			x = 4+q6
			x = q6-q6
			g8 = 1*g8
			paths.append(3)
		else:
			g8 = g8+g8
			g8 = g8*7
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		g8 = q6**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))