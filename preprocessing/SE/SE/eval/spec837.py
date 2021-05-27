import numpy as np 

def function(x):

	q7 = x
	g0 = x
	paths = []
	try:
		if x > 7:
			x = g0/q7
			paths.append(1)
		else:
			q7 = q7/3
			g0 = g0-9
			q7 = q7/6
			paths.append(2)
		if g0 >= 6:
			g0 = q7-g0
			q7 = q7+2
			g0 = 9-g0
			paths.append(3)
		else:
			q7 = x*2
			g0 = x/g0
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))