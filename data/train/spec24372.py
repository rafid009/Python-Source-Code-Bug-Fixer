import numpy as np 

def function(x):

	s1 = 9
	f9 = x
	paths = []
	try:
		if s1 >= 4:
			s1 = s1-6
			x = 6*7
			x = 6-3
			paths.append(1)
		else:
			f9 = f9/6
			paths.append(2)
		if f9 > 8:
			s1 = 2/5
			x = x-7
			s1 = s1-f9
			paths.append(3)
		else:
			s1 = 3/s1
			x = 8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))