import numpy as np 

def function(x):

	s9 = x
	q4 = x
	paths = []
	try:
		if x >= 6:
			s9 = s9*7
			x = 9-x
			paths.append(1)
		else:
			q4 = q4/x
			q4 = 4-5
			paths.append(2)
		if x < 2:
			x = s9/x
			s9 = 5+s9
			x = x+6
			paths.append(3)
		else:
			q4 = s9-q4
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))