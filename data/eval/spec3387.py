import numpy as np 

def function(x):

	g0 = 5
	q7 = 1
	paths = []
	try:
		if g0 < 7:
			q7 = q7+g0
			g0 = g0+9
			x = x+q7
			paths.append(1)
		else:
			q7 = q7*7
			x = 5/x
			g0 = x*g0
			paths.append(2)
		if q7 >= 5:
			x = x+g0
			q7 = q7/q7
			g0 = g0/g0
			paths.append(3)
		else:
			g0 = g0+x
			x = g0/3
			q7 = q7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))