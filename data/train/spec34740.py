import numpy as np 

def function(x):

	g2 = 3
	s0 = 9
	x = 5
	paths = []
	try:
		if s0 < 7:
			x = x/x
			x = x*4
			g2 = g2-4
			paths.append(1)
		else:
			g2 = 6/g2
			g2 = g2/g2
			x = x/4
			paths.append(2)
		if s0 <= 7:
			g2 = g2*3
			g2 = 9+8
			s0 = s0*6
			paths.append(3)
		else:
			g2 = 0-g2
			s0 = x+s0
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))