import numpy as np 

def function(x):

	r7 = x
	g6 = 5
	paths = []
	try:
		if r7 >= 2:
			g6 = g6-r7
			r7 = 2-r7
			r7 = r7/6
			paths.append(1)
		else:
			g6 = 2+g6
			r7 = g6*r7
			r7 = 4/r7
			paths.append(2)
		if g6 > 4:
			x = x*6
			r7 = r7*7
			paths.append(3)
		else:
			r7 = r7/r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))