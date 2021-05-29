import numpy as np 

def function(x):

	g7 = x
	s5 = 9
	paths = []
	try:
		if s5 > 8:
			x = 1*7
			paths.append(1)
		else:
			g7 = s5-8
			paths.append(2)
		if g7 <= 8:
			s5 = 7+g7
			s5 = g7-4
			paths.append(3)
		else:
			x = 0*0
			x = 3/7
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		g7 = s5**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))