import numpy as np 

def function(x):

	s4 = x
	j0 = x
	paths = []
	try:
		if x <= 1:
			x = x*5
			s4 = s4*6
			paths.append(1)
		else:
			s4 = 9-x
			j0 = s4-5
			paths.append(2)
		if s4 <= 1:
			x = 5/7
			x = j0+j0
			j0 = 8*j0
			paths.append(3)
		else:
			j0 = j0/4
			x = x-x
			s4 = s4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))