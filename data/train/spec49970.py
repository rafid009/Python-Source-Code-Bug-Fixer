import numpy as np 

def function(x):

	l8 = 3
	g8 = 7
	paths = []
	try:
		if l8 >= 9:
			g8 = 7*5
			paths.append(1)
		else:
			g8 = 0-7
			l8 = l8+9
			paths.append(2)
		if x >= 4:
			g8 = g8*3
			g8 = 1-g8
			paths.append(3)
		else:
			x = 1+g8
			g8 = 2/g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		l8 = g8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))