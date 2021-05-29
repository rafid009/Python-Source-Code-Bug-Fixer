import numpy as np 

def function(x):

	s6 = 2
	g8 = 5
	paths = []
	try:
		if g8 >= 1:
			s6 = s6+s6
			s6 = 1+s6
			x = x+6
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if s6 <= 6:
			x = x*s6
			s6 = s6*x
			g8 = s6*3
			paths.append(3)
		else:
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))