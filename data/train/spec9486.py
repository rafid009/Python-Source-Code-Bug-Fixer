import numpy as np 

def function(x):

	s1 = 7
	d4 = 3
	paths = []
	try:
		if d4 > 8:
			d4 = s1-8
			s1 = s1-x
			x = x/1
			paths.append(1)
		else:
			s1 = 0/9
			paths.append(2)
		if s1 <= 0:
			d4 = 6-d4
			paths.append(3)
		else:
			d4 = x*8
			x = x-5
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