import numpy as np 

def function(x):

	q9 = 7
	g8 = x
	paths = []
	try:
		if g8 > 4:
			q9 = 2*q9
			paths.append(1)
		else:
			q9 = q9*q9
			q9 = 4-q9
			paths.append(2)
		if x >= 9:
			g8 = q9/5
			x = q9-x
			g8 = 7/g8
			paths.append(3)
		else:
			g8 = g8*q9
			g8 = 1*g8
			x = x-5
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		g8 = q9**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))