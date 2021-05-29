import numpy as np 

def function(x):

	s5 = 8
	g3 = 3
	paths = []
	try:
		if s5 > 0:
			g3 = g3-5
			s5 = 5+9
			paths.append(1)
		else:
			g3 = g3/g3
			g3 = s5*4
			paths.append(2)
		if x > 8:
			x = 8*x
			x = 7*x
			paths.append(3)
		else:
			g3 = 6*g3
			x = 2/s5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))