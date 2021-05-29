import numpy as np 

def function(x):

	s7 = 1
	g1 = 0
	paths = []
	try:
		if g1 > 1:
			x = s7/x
			x = x/6
			g1 = 4*1
			paths.append(1)
		else:
			g1 = g1*4
			paths.append(2)
		if g1 > 5:
			s7 = 0+g1
			paths.append(3)
		else:
			g1 = 8+x
			g1 = 2*g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		s7 = g1**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))