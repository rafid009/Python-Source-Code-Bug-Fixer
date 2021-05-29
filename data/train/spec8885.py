import numpy as np 

def function(x):

	r1 = x
	g3 = 1
	paths = []
	try:
		if x <= 1:
			x = 2-x
			paths.append(1)
		else:
			g3 = g3-9
			x = 4/x
			paths.append(2)
		if g3 < 3:
			r1 = 9*r1
			paths.append(3)
		else:
			x = g3/5
			r1 = 7+3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		g3 = r1**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))