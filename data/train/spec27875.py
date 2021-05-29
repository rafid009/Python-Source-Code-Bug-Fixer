import numpy as np 

def function(x):

	s0 = x
	j0 = 1
	paths = []
	try:
		if j0 >= 0:
			x = x-2
			j0 = 5*j0
			paths.append(1)
		else:
			s0 = s0-5
			s0 = x+s0
			paths.append(2)
		if x <= 2:
			x = 7+x
			j0 = j0/7
			j0 = j0/5
			paths.append(3)
		else:
			x = 5*x
			s0 = 1*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))