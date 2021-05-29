import numpy as np 

def function(x):

	g6 = x
	r0 = x
	x = 5
	paths = []
	try:
		if x > 3:
			x = g6*0
			g6 = 3/g6
			paths.append(1)
		else:
			g6 = 9+5
			g6 = 6/r0
			paths.append(2)
		if g6 >= 4:
			g6 = g6/8
			r0 = x/r0
			paths.append(3)
		else:
			x = 1+g6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))