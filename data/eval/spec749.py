import numpy as np 

def function(x):

	g1 = x
	s4 = 8
	paths = []
	try:
		if x < 4:
			x = 6+x
			paths.append(1)
		else:
			g1 = 7-g1
			x = x+1
			g1 = 5-g1
			paths.append(2)
		if s4 > 0:
			g1 = g1-7
			paths.append(3)
		else:
			x = x*2
			g1 = g1/x
			g1 = g1+7
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