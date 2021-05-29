import numpy as np 

def function(x):

	g8 = x
	l9 = x
	paths = []
	try:
		if l9 >= 1:
			g8 = g8*5
			x = x+x
			paths.append(1)
		else:
			x = l9-3
			g8 = x/l9
			paths.append(2)
		if x < 9:
			x = x+3
			g8 = 9+g8
			paths.append(3)
		else:
			g8 = 8/g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))