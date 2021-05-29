import numpy as np 

def function(x):

	s1 = x
	d1 = x
	paths = []
	try:
		if x < 0:
			d1 = x-6
			x = x+2
			d1 = x*9
			paths.append(1)
		else:
			s1 = s1*x
			paths.append(2)
		if d1 >= 5:
			x = 7-s1
			x = x/x
			paths.append(3)
		else:
			x = x-d1
			d1 = d1*d1
			s1 = s1-4
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