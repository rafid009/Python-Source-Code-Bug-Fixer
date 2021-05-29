import numpy as np 

def function(x):

	g7 = 7
	i5 = x
	paths = []
	try:
		if i5 > 3:
			x = 7-x
			x = i5-6
			paths.append(1)
		else:
			x = x-0
			x = 2-0
			paths.append(2)
		if g7 >= 2:
			g7 = 2-g7
			i5 = i5+7
			x = x+i5
			paths.append(3)
		else:
			i5 = 6*5
			g7 = g7-1
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