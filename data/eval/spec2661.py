import numpy as np 

def function(x):

	q6 = 0
	g6 = x
	paths = []
	try:
		if x <= 8:
			x = 5+x
			g6 = g6+1
			paths.append(1)
		else:
			q6 = g6/g6
			x = g6/7
			x = x+q6
			paths.append(2)
		if x < 0:
			x = x-7
			q6 = q6-9
			paths.append(3)
		else:
			q6 = 4/6
			x = x/5
			x = g6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))