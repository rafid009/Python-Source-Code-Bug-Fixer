import numpy as np 

def function(x):

	a4 = x
	g3 = x
	paths = []
	try:
		if a4 >= 9:
			x = x*3
			a4 = a4/x
			g3 = x*8
			paths.append(1)
		else:
			g3 = 6+3
			a4 = a4+g3
			a4 = 6+3
			paths.append(2)
		if a4 <= 0:
			a4 = g3*1
			x = x-x
			a4 = 9*x
			paths.append(3)
		else:
			g3 = 6/2
			a4 = 5+a4
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