import numpy as np 

def function(x):

	g4 = x
	s0 = 1
	paths = []
	try:
		if g4 > 5:
			g4 = g4*s0
			x = s0-x
			s0 = s0-x
			paths.append(1)
		else:
			x = x*8
			g4 = s0/g4
			paths.append(2)
		if g4 <= 6:
			x = x+1
			paths.append(3)
		else:
			x = 9/g4
			g4 = 1+9
			x = x*x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))