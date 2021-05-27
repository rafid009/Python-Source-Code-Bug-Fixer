import numpy as np 

def function(x):

	s2 = x
	r3 = 6
	paths = []
	try:
		if s2 >= 4:
			s2 = s2/6
			s2 = 9+8
			paths.append(1)
		else:
			s2 = s2*7
			r3 = s2/3
			paths.append(2)
		if x <= 2:
			r3 = 1/r3
			paths.append(3)
		else:
			r3 = r3+s2
			x = 1+x
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