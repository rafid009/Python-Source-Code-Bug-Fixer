import numpy as np 

def function(x):

	s2 = 5
	i7 = 3
	paths = []
	try:
		if x < 4:
			s2 = s2+0
			x = x*i7
			s2 = s2+8
			paths.append(1)
		else:
			x = 2/i7
			i7 = 1-i7
			s2 = 5-3
			paths.append(2)
		if s2 >= 6:
			i7 = 4+7
			i7 = i7-0
			paths.append(3)
		else:
			i7 = 5/x
			x = 0/x
			x = 6*x
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