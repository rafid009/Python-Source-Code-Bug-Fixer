import numpy as np 

def function(x):

	s4 = 1
	t8 = 5
	paths = []
	try:
		if t8 >= 2:
			s4 = t8-x
			paths.append(1)
		else:
			x = t8+x
			s4 = 1*s4
			paths.append(2)
		if s4 < 5:
			x = 0/9
			s4 = s4*1
			s4 = s4+t8
			paths.append(3)
		else:
			x = t8-x
			s4 = 1*s4
			x = x-t8
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