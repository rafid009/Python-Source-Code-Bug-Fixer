import numpy as np 

def function(x):

	g8 = 4
	s5 = 4
	paths = []
	try:
		if s5 < 0:
			g8 = g8-1
			x = x+9
			paths.append(1)
		else:
			x = s5-x
			paths.append(2)
		if x > 0:
			x = x*7
			g8 = 0/g8
			g8 = 7-s5
			paths.append(3)
		else:
			g8 = g8*s5
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))