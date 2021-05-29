import numpy as np 

def function(x):

	j0 = x
	s4 = 6
	paths = []
	try:
		if x < 2:
			s4 = 9+1
			s4 = 0-s4
			paths.append(1)
		else:
			j0 = x-j0
			paths.append(2)
		if j0 < 9:
			s4 = 3*s4
			paths.append(3)
		else:
			j0 = j0*x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))