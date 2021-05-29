import numpy as np 

def function(x):

	t0 = 9
	s9 = x
	x = x
	paths = []
	try:
		if s9 <= 2:
			s9 = s9-t0
			paths.append(1)
		else:
			x = 3/8
			t0 = x/t0
			paths.append(2)
		if s9 <= 9:
			s9 = 5+s9
			t0 = 1-s9
			s9 = s9/8
			paths.append(3)
		else:
			t0 = s9-2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))