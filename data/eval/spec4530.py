import numpy as np 

def function(x):

	t3 = 5
	s4 = 7
	paths = []
	try:
		if s4 > 1:
			s4 = x*x
			t3 = s4*t3
			s4 = s4/x
			paths.append(1)
		else:
			s4 = x*s4
			t3 = 5-t3
			paths.append(2)
		if t3 <= 1:
			t3 = t3-2
			paths.append(3)
		else:
			t3 = x-s4
			x = t3-2
			t3 = t3/4
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