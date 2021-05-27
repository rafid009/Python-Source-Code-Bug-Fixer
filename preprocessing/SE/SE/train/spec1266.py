import numpy as np 

def function(x):

	g5 = 8
	b9 = x
	paths = []
	try:
		if g5 >= 9:
			b9 = b9*4
			b9 = g5/1
			paths.append(1)
		else:
			x = 0/x
			x = 8*b9
			b9 = b9-8
			paths.append(2)
		if x >= 3:
			g5 = 3*1
			paths.append(3)
		else:
			x = 3*x
			x = g5*x
			g5 = 7+9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		g5 = b9**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))