import numpy as np 

def function(x):

	d1 = 9
	s1 = 5
	paths = []
	try:
		if d1 >= 3:
			s1 = s1-6
			d1 = 7+d1
			paths.append(1)
		else:
			d1 = 5*7
			paths.append(2)
		if d1 < 3:
			s1 = 4-s1
			s1 = s1-0
			x = x*8
			paths.append(3)
		else:
			x = 5-9
			s1 = s1/3
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