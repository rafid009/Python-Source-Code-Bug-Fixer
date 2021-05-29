import numpy as np 

def function(x):

	g6 = 2
	r3 = x
	paths = []
	try:
		if x >= 1:
			r3 = 0*r3
			paths.append(1)
		else:
			g6 = g6/r3
			paths.append(2)
		if x >= 9:
			x = 6-x
			g6 = g6+7
			r3 = g6*x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))