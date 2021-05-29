import numpy as np 

def function(x):

	g4 = 3
	s1 = x
	paths = []
	try:
		if x >= 8:
			x = x+1
			paths.append(1)
		else:
			x = x-3
			s1 = 8+s1
			paths.append(2)
		if s1 < 2:
			g4 = s1-8
			g4 = g4*0
			paths.append(3)
		else:
			x = x+g4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		g4 = s1**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))