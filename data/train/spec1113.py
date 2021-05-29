import numpy as np 

def function(x):

	o4 = x
	g3 = 7
	paths = []
	try:
		if x < 5:
			g3 = 8*9
			g3 = g3*g3
			paths.append(1)
		else:
			g3 = g3-0
			paths.append(2)
		if x <= 1:
			g3 = g3+g3
			g3 = o4*g3
			g3 = g3+6
			paths.append(3)
		else:
			o4 = o4-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))