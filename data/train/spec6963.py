import numpy as np 

def function(x):

	x2 = 6
	s4 = 3
	paths = []
	try:
		if s4 <= 1:
			s4 = s4+1
			x = 0-9
			s4 = 1*4
			paths.append(1)
		else:
			s4 = 1+4
			x2 = 9-5
			s4 = 0+x
			paths.append(2)
		if s4 > 8:
			s4 = 7+9
			paths.append(3)
		else:
			x = s4+x
			x2 = x2-5
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		s4 = x2**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))