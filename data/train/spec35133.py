import numpy as np 

def function(x):

	x0 = x
	s6 = x
	paths = []
	try:
		if s6 > 5:
			x = x+1
			x = 6-5
			s6 = x-s6
			paths.append(1)
		else:
			x = 1-x
			x = 9/x
			paths.append(2)
		if x0 > 0:
			x = x/x
			x0 = 6-x0
			paths.append(3)
		else:
			x = 9+3
			s6 = 2*x0
			x = x+1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x0 = s6**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))