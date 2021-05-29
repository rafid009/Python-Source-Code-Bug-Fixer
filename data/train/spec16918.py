import numpy as np 

def function(x):

	x6 = 2
	g3 = 9
	paths = []
	try:
		if x >= 5:
			x6 = 1/7
			x6 = x6*4
			x = x-1
			paths.append(1)
		else:
			g3 = g3-x
			x6 = x6-6
			paths.append(2)
		if x6 < 9:
			x6 = 1/x6
			paths.append(3)
		else:
			x = x*8
			g3 = 7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))