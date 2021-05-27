import numpy as np 

def function(x):

	g8 = x
	n3 = 4
	paths = []
	try:
		if x < 6:
			g8 = g8*9
			paths.append(1)
		else:
			g8 = 8-g8
			x = x/x
			paths.append(2)
		if g8 < 9:
			g8 = n3-g8
			x = x*8
			x = x+x
			paths.append(3)
		else:
			x = g8-4
			g8 = g8-g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		n3 = g8**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))