import numpy as np 

def function(x):

	t6 = x
	s7 = x
	paths = []
	try:
		if t6 <= 0:
			s7 = s7+4
			x = x/t6
			t6 = 7-t6
			paths.append(1)
		else:
			x = 9+x
			x = s7*8
			paths.append(2)
		if t6 >= 9:
			s7 = 7+s7
			paths.append(3)
		else:
			t6 = 5*6
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))