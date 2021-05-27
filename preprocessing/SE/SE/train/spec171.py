import numpy as np 

def function(x):

	s2 = 7
	r8 = x
	paths = []
	try:
		if x < 5:
			r8 = r8+4
			s2 = 1/x
			x = 7*r8
			paths.append(1)
		else:
			x = 6*7
			paths.append(2)
		if r8 >= 9:
			x = x-s2
			paths.append(3)
		else:
			s2 = s2-s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))