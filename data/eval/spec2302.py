import numpy as np 

def function(x):

	x8 = x
	g9 = 6
	paths = []
	try:
		if x < 2:
			g9 = g9*2
			x = x/1
			paths.append(1)
		else:
			x8 = x8*3
			paths.append(2)
		if x8 <= 4:
			x = x-g9
			paths.append(3)
		else:
			x8 = x8/x8
			x = x*x8
			x8 = 5/x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		g9 = x8**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))