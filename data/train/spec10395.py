import numpy as np 

def function(x):

	x6 = 4
	g9 = x
	paths = []
	try:
		if x6 < 1:
			x = x/1
			g9 = 8*2
			x = x+5
			paths.append(1)
		else:
			x6 = g9-x6
			g9 = g9/3
			paths.append(2)
		if g9 > 0:
			g9 = 7/g9
			x6 = x-7
			x6 = x-x6
			paths.append(3)
		else:
			x = x-7
			x6 = x6-x6
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