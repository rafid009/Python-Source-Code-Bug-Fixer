import numpy as np 

def function(x):

	s4 = x
	g8 = 1
	paths = []
	try:
		if s4 < 4:
			x = x+8
			x = x+7
			paths.append(1)
		else:
			x = 9+x
			g8 = 5/x
			s4 = g8/g8
			paths.append(2)
		if g8 < 2:
			x = x+8
			x = g8+0
			paths.append(3)
		else:
			g8 = 1-x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))