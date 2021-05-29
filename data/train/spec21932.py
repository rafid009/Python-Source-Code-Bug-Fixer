import numpy as np 

def function(x):

	g7 = x
	b8 = 8
	paths = []
	try:
		if b8 > 0:
			g7 = g7*5
			b8 = b8-x
			paths.append(1)
		else:
			x = g7/6
			paths.append(2)
		if b8 >= 8:
			b8 = x+1
			b8 = g7*b8
			b8 = x-2
			paths.append(3)
		else:
			b8 = b8+1
			g7 = g7-9
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))