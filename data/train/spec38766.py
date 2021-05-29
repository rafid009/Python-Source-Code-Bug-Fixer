import numpy as np 

def function(x):

	j4 = x
	s6 = 9
	paths = []
	try:
		if x <= 1:
			s6 = 6*j4
			paths.append(1)
		else:
			j4 = 6-s6
			s6 = s6-8
			paths.append(2)
		if x >= 5:
			s6 = s6-s6
			paths.append(3)
		else:
			j4 = j4/2
			x = 3*s6
			s6 = x+s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))