import numpy as np 

def function(x):

	s5 = x
	g1 = 8
	paths = []
	try:
		if x > 8:
			s5 = s5/9
			g1 = s5+g1
			s5 = x+s5
			paths.append(1)
		else:
			g1 = 4*g1
			g1 = 0-g1
			paths.append(2)
		if g1 >= 1:
			g1 = g1-6
			g1 = 4-g1
			paths.append(3)
		else:
			s5 = 0+s5
			x = x*6
			g1 = g1/6
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		s5 = g1**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))