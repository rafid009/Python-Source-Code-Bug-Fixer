import numpy as np 

def function(x):

	g3 = x
	s0 = x
	paths = []
	try:
		if x <= 0:
			s0 = 9/s0
			paths.append(1)
		else:
			s0 = s0-7
			paths.append(2)
		if g3 <= 2:
			x = x-5
			paths.append(3)
		else:
			s0 = 6/8
			g3 = 2-7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		s0 = g3**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))