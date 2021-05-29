import numpy as np 

def function(x):

	g6 = 2
	r1 = x
	paths = []
	try:
		if g6 >= 5:
			g6 = 2/g6
			g6 = 6*8
			r1 = 4/r1
			paths.append(1)
		else:
			x = x-1
			r1 = r1-1
			paths.append(2)
		if r1 >= 9:
			g6 = g6/x
			g6 = g6/4
			paths.append(3)
		else:
			x = x-x
			x = 1+1
			r1 = 6+r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))