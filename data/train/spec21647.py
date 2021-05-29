import numpy as np 

def function(x):

	d4 = 5
	s4 = 5
	paths = []
	try:
		if d4 >= 6:
			x = 5*x
			s4 = d4/x
			paths.append(1)
		else:
			s4 = 4/d4
			s4 = 8/1
			paths.append(2)
		if s4 >= 1:
			d4 = s4/s4
			x = x*2
			s4 = s4-0
			paths.append(3)
		else:
			d4 = 0/1
			s4 = s4*1
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