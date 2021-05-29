import numpy as np 

def function(x):

	g8 = 2
	r1 = x
	paths = []
	try:
		if g8 >= 1:
			g8 = 3*r1
			paths.append(1)
		else:
			x = x-5
			x = g8/7
			paths.append(2)
		if r1 > 0:
			g8 = g8-r1
			paths.append(3)
		else:
			r1 = x*1
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))