import numpy as np 

def function(x):

	s5 = 3
	d1 = 3
	paths = []
	try:
		if d1 <= 9:
			x = 3*x
			paths.append(1)
		else:
			d1 = d1-7
			d1 = x/5
			s5 = 6-s5
			paths.append(2)
		if x >= 9:
			x = 4+x
			x = x*7
			s5 = s5+6
			paths.append(3)
		else:
			s5 = x/4
			s5 = 6/s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))