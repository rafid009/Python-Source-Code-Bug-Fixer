import numpy as np 

def function(x):

	q4 = 3
	g0 = 5
	paths = []
	try:
		if x <= 1:
			g0 = g0/3
			paths.append(1)
		else:
			g0 = 3+g0
			paths.append(2)
		if q4 <= 0:
			g0 = 0-g0
			x = 3*0
			paths.append(3)
		else:
			q4 = q4*4
			q4 = 2+q4
			q4 = x/q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		g0 = q4**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))