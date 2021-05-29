import numpy as np 

def function(x):

	g6 = 8
	s4 = x
	paths = []
	try:
		if g6 >= 5:
			s4 = s4*4
			paths.append(1)
		else:
			x = s4+x
			x = 9/x
			paths.append(2)
		if x > 9:
			g6 = x*1
			x = 6*4
			paths.append(3)
		else:
			x = 4*3
			g6 = 7-g6
			g6 = 6*s4
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))