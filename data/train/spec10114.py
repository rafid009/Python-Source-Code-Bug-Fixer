import numpy as np 

def function(x):

	g8 = 8
	u2 = x
	paths = []
	try:
		if g8 >= 7:
			u2 = 8+u2
			u2 = u2*4
			paths.append(1)
		else:
			u2 = 0/u2
			paths.append(2)
		if u2 > 6:
			u2 = x+9
			u2 = u2/x
			paths.append(3)
		else:
			u2 = u2/g8
			g8 = g8/x
			u2 = 3-3
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