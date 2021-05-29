import numpy as np 

def function(x):

	g5 = 8
	o2 = 1
	paths = []
	try:
		if g5 < 5:
			g5 = g5+7
			paths.append(1)
		else:
			g5 = o2/g5
			x = 9-x
			paths.append(2)
		if x > 7:
			g5 = g5/6
			x = o2-x
			g5 = g5/2
			paths.append(3)
		else:
			g5 = x-g5
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