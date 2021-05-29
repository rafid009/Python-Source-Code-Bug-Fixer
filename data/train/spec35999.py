import numpy as np 

def function(x):

	s1 = 8
	d0 = x
	x = 5
	paths = []
	try:
		if x < 6:
			x = 1-2
			paths.append(1)
		else:
			d0 = 6+d0
			paths.append(2)
		if s1 > 9:
			d0 = d0*1
			s1 = 7-8
			paths.append(3)
		else:
			d0 = 6*4
			d0 = 0*x
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