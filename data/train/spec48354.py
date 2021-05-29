import numpy as np 

def function(x):

	s4 = x
	i4 = x
	paths = []
	try:
		if s4 < 2:
			i4 = i4+7
			i4 = 8-0
			s4 = s4+x
			paths.append(1)
		else:
			x = x+x
			x = x+x
			s4 = s4/s4
			paths.append(2)
		if s4 >= 1:
			x = x*x
			i4 = 9*5
			paths.append(3)
		else:
			i4 = 6+i4
			i4 = 7/s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))