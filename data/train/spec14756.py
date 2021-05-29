import numpy as np 

def function(x):

	s7 = 2
	q9 = x
	paths = []
	try:
		if q9 > 0:
			x = 2-x
			x = 9/x
			paths.append(1)
		else:
			x = 1-x
			s7 = s7+5
			paths.append(2)
		if x <= 4:
			x = x+2
			s7 = 6+s7
			paths.append(3)
		else:
			s7 = q9+7
			s7 = s7+s7
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