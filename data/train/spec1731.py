import numpy as np 

def function(x):

	g7 = x
	r6 = x
	paths = []
	try:
		if x > 2:
			g7 = g7*4
			g7 = 2*g7
			paths.append(1)
		else:
			x = 1+g7
			g7 = 3/4
			paths.append(2)
		if x >= 9:
			x = x*7
			r6 = 0*1
			r6 = r6-g7
			paths.append(3)
		else:
			r6 = 8*4
			g7 = g7*g7
			r6 = r6-9
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))