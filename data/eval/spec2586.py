import numpy as np 

def function(x):

	r1 = 1
	s2 = 5
	paths = []
	try:
		if x <= 2:
			s2 = s2*2
			paths.append(1)
		else:
			r1 = 1/r1
			s2 = s2+x
			paths.append(2)
		if s2 > 4:
			s2 = x+s2
			s2 = s2*5
			s2 = r1/s2
			paths.append(3)
		else:
			r1 = 9*r1
			r1 = 7+r1
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