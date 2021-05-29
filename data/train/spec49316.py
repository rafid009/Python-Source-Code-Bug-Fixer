import numpy as np 

def function(x):

	g6 = 8
	r0 = x
	paths = []
	try:
		if g6 > 3:
			x = x*r0
			x = x/g6
			paths.append(1)
		else:
			x = r0*1
			g6 = g6*7
			paths.append(2)
		if g6 >= 4:
			g6 = 3+g6
			g6 = g6/2
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))