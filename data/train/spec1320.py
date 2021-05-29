import numpy as np 

def function(x):

	q7 = 1
	g0 = x
	paths = []
	try:
		if g0 > 2:
			x = 6+x
			g0 = g0+3
			paths.append(1)
		else:
			q7 = 9+q7
			g0 = g0/7
			paths.append(2)
		if x < 0:
			x = g0/6
			q7 = q7*9
			paths.append(3)
		else:
			q7 = 4*q7
			q7 = q7/9
			g0 = 8/g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))