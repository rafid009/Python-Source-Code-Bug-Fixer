import numpy as np 

def function(x):

	s7 = x
	g8 = x
	paths = []
	try:
		if x < 5:
			x = x+4
			x = x*2
			paths.append(1)
		else:
			g8 = g8-g8
			x = s7/s7
			paths.append(2)
		if x > 7:
			s7 = g8*4
			paths.append(3)
		else:
			g8 = 7+8
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))