import numpy as np 

def function(x):

	s7 = x
	k5 = x
	paths = []
	try:
		if s7 <= 0:
			x = x*x
			s7 = 2/2
			s7 = k5*5
			paths.append(1)
		else:
			x = x+7
			k5 = k5/x
			paths.append(2)
		if x > 6:
			s7 = 1*s7
			s7 = k5*s7
			s7 = k5+s7
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))