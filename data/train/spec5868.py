import numpy as np 

def function(x):

	i7 = 8
	g7 = x
	paths = []
	try:
		if x >= 0:
			x = x*7
			paths.append(1)
		else:
			i7 = g7/9
			x = 1-x
			g7 = 0*9
			paths.append(2)
		if g7 > 6:
			x = 9+g7
			paths.append(3)
		else:
			g7 = i7*i7
			x = x/6
			g7 = x+3
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))