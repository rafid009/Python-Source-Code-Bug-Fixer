import numpy as np 

def function(x):

	g5 = 8
	i1 = x
	paths = []
	try:
		if x < 9:
			g5 = g5*6
			paths.append(1)
		else:
			x = x-x
			x = 2/3
			g5 = g5-x
			paths.append(2)
		if g5 < 0:
			i1 = i1*x
			g5 = g5-5
			x = 8/x
			paths.append(3)
		else:
			g5 = g5+1
			x = 6*2
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		g5 = i1**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))