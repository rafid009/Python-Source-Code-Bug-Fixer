import numpy as np 

def function(x):

	g6 = 1
	q0 = 1
	paths = []
	try:
		if x >= 8:
			g6 = x*g6
			g6 = q0+0
			q0 = q0+9
			paths.append(1)
		else:
			g6 = 1+7
			paths.append(2)
		if q0 > 8:
			g6 = 7-6
			q0 = g6-7
			q0 = q0+q0
			paths.append(3)
		else:
			g6 = x*x
			g6 = x+2
			g6 = g6-8
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))