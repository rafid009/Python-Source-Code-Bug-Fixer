import numpy as np 

def function(x):

	g7 = x
	b7 = x
	paths = []
	try:
		if b7 < 3:
			g7 = 8+3
			b7 = b7+9
			paths.append(1)
		else:
			g7 = g7-5
			x = x+4
			x = b7+x
			paths.append(2)
		if b7 >= 6:
			b7 = 8/b7
			x = 5*b7
			paths.append(3)
		else:
			b7 = b7/g7
			b7 = x-4
			b7 = b7/g7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		b7 = g7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))