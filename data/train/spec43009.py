import numpy as np 

def function(x):

	g3 = x
	r6 = 2
	x = x
	paths = []
	try:
		if x >= 8:
			r6 = r6-4
			paths.append(1)
		else:
			g3 = g3+3
			x = x+2
			paths.append(2)
		if r6 >= 9:
			g3 = g3*x
			g3 = x/1
			r6 = 8+r6
			paths.append(3)
		else:
			r6 = x-6
			x = 0-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))