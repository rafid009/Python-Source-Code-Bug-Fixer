import numpy as np 

def function(x):

	i4 = x
	s6 = 1
	paths = []
	try:
		if i4 >= 2:
			x = 6*s6
			paths.append(1)
		else:
			s6 = 0/s6
			i4 = 5/x
			x = x/9
			paths.append(2)
		if x <= 7:
			s6 = s6-9
			paths.append(3)
		else:
			x = 9+x
			i4 = x-7
			x = x+s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))