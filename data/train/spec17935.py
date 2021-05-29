import numpy as np 

def function(x):

	b2 = x
	s8 = x
	x = 1
	paths = []
	try:
		if b2 > 3:
			b2 = b2+2
			x = 1*x
			s8 = s8-s8
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x <= 2:
			x = 3/x
			s8 = x+s8
			s8 = 6*s8
			paths.append(3)
		else:
			s8 = 9/s8
			x = x-b2
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		s8 = b2**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))