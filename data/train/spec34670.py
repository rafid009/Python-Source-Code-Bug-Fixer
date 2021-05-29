import numpy as np 

def function(x):

	t6 = x
	s4 = x
	paths = []
	try:
		if x < 1:
			x = x*x
			s4 = s4+x
			paths.append(1)
		else:
			t6 = 0+t6
			paths.append(2)
		if s4 >= 0:
			t6 = 7-s4
			s4 = 5*x
			paths.append(3)
		else:
			t6 = t6+x
			x = x-s4
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		s4 = t6**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))