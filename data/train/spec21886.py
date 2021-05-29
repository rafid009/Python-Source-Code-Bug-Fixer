import numpy as np 

def function(x):

	f7 = 3
	g8 = 0
	x = 6
	paths = []
	try:
		if g8 >= 7:
			f7 = f7+6
			paths.append(1)
		else:
			f7 = 8*f7
			g8 = 7-g8
			paths.append(2)
		if x < 6:
			f7 = 2/1
			g8 = 0-g8
			f7 = f7+g8
			paths.append(3)
		else:
			f7 = f7*2
			g8 = 8-f7
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