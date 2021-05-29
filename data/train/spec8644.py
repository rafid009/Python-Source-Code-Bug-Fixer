import numpy as np 

def function(x):

	g4 = 2
	s4 = 5
	paths = []
	try:
		if g4 >= 4:
			x = x*5
			g4 = 5/2
			x = x-0
			paths.append(1)
		else:
			s4 = s4+x
			x = g4-7
			paths.append(2)
		if x < 9:
			g4 = g4+7
			s4 = 7/s4
			paths.append(3)
		else:
			g4 = 4+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))