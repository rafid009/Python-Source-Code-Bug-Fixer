import numpy as np 

def function(x):

	s4 = 9
	e2 = x
	paths = []
	try:
		if x <= 5:
			e2 = e2*3
			s4 = s4+2
			s4 = 3/8
			paths.append(1)
		else:
			e2 = 2/4
			x = s4+2
			paths.append(2)
		if s4 < 1:
			e2 = 7-e2
			s4 = 4-s4
			paths.append(3)
		else:
			e2 = s4/1
			s4 = e2-2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		s4 = e2**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))