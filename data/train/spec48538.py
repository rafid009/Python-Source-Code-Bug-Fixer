import numpy as np 

def function(x):

	r7 = x
	g5 = x
	paths = []
	try:
		if g5 >= 3:
			g5 = 6+g5
			g5 = g5+r7
			g5 = 1*x
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if r7 <= 9:
			r7 = 3*r7
			x = 9*x
			g5 = 7/g5
			paths.append(3)
		else:
			g5 = 1*r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		g5 = r7**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))