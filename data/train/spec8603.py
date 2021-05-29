import numpy as np 

def function(x):

	g2 = 6
	s8 = 1
	paths = []
	try:
		if g2 < 0:
			x = x*s8
			g2 = g2+s8
			x = x+1
			paths.append(1)
		else:
			g2 = 7-5
			g2 = 7*g2
			g2 = 3-4
			paths.append(2)
		if g2 >= 8:
			s8 = s8-1
			paths.append(3)
		else:
			x = 9+9
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))