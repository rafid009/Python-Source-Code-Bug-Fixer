import numpy as np 

def function(x):

	s1 = 2
	h3 = 5
	paths = []
	try:
		if x > 5:
			x = x*8
			paths.append(1)
		else:
			s1 = s1*h3
			paths.append(2)
		if s1 >= 4:
			s1 = s1+4
			paths.append(3)
		else:
			x = 4-8
			x = 1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))