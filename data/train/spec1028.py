import numpy as np 

def function(x):

	g0 = 7
	s9 = x
	paths = []
	try:
		if x > 6:
			s9 = x+s9
			s9 = 1*s9
			paths.append(1)
		else:
			g0 = x/g0
			paths.append(2)
		if g0 > 0:
			x = s9+s9
			x = x/5
			paths.append(3)
		else:
			s9 = 9/7
			s9 = 6-s9
			s9 = x*9
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		s9 = g0**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))