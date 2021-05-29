import numpy as np 

def function(x):

	g0 = x
	s5 = x
	paths = []
	try:
		if x >= 4:
			g0 = g0/7
			s5 = s5-3
			paths.append(1)
		else:
			x = 3-9
			paths.append(2)
		if g0 <= 5:
			x = x*4
			s5 = x+x
			x = 1*s5
			paths.append(3)
		else:
			g0 = 6/5
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))