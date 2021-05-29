import numpy as np 

def function(x):

	u6 = 5
	g4 = x
	paths = []
	try:
		if u6 <= 1:
			u6 = 3-0
			paths.append(1)
		else:
			g4 = g4+8
			u6 = u6-6
			paths.append(2)
		if u6 <= 3:
			g4 = 1/g4
			x = x+1
			paths.append(3)
		else:
			x = x-4
			g4 = x/1
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))