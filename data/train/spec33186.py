import numpy as np 

def function(x):

	z4 = x
	s6 = x
	paths = []
	try:
		if x < 0:
			x = x*2
			paths.append(1)
		else:
			x = x-9
			s6 = s6-2
			paths.append(2)
		if s6 <= 3:
			x = s6/x
			paths.append(3)
		else:
			s6 = s6*z4
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		z4 = s6**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))