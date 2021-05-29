import numpy as np 

def function(x):

	g3 = 8
	s0 = x
	paths = []
	try:
		if s0 >= 8:
			g3 = 9+g3
			g3 = 0*2
			paths.append(1)
		else:
			x = 8+s0
			g3 = g3*s0
			s0 = s0-4
			paths.append(2)
		if g3 <= 9:
			s0 = x/7
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))