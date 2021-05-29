import numpy as np 

def function(x):

	s4 = x
	q1 = 9
	paths = []
	try:
		if x > 3:
			s4 = s4+3
			x = x*x
			paths.append(1)
		else:
			s4 = s4+4
			s4 = 5*6
			paths.append(2)
		if s4 <= 7:
			x = x/q1
			paths.append(3)
		else:
			s4 = x/s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))