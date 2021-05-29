import numpy as np 

def function(x):

	b6 = x
	s2 = 9
	paths = []
	try:
		if b6 < 1:
			s2 = s2*x
			paths.append(1)
		else:
			s2 = 0-s2
			b6 = b6-x
			paths.append(2)
		if x <= 4:
			x = 7+6
			x = b6*4
			paths.append(3)
		else:
			s2 = s2+1
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		s2 = b6**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))