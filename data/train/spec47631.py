import numpy as np 

def function(x):

	g9 = 2
	x9 = x
	paths = []
	try:
		if x >= 6:
			x = x*5
			g9 = 6*1
			paths.append(1)
		else:
			g9 = x+g9
			paths.append(2)
		if x9 < 4:
			g9 = x+x9
			g9 = 1/g9
			x = 3/x
			paths.append(3)
		else:
			g9 = g9-x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))