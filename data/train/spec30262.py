import numpy as np 

def function(x):

	n1 = x
	s8 = x
	x = 0
	paths = []
	try:
		if s8 <= 4:
			x = x+x
			x = x*x
			x = 7-s8
			paths.append(1)
		else:
			n1 = x+6
			n1 = 1+n1
			paths.append(2)
		if n1 < 5:
			x = 0*x
			paths.append(3)
		else:
			s8 = 7+s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))