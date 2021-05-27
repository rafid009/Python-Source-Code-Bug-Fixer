import numpy as np 

def function(x):

	s5 = x
	s4 = 2
	paths = []
	try:
		if s4 > 1:
			s4 = x+s4
			paths.append(1)
		else:
			s4 = s5/s4
			paths.append(2)
		if s4 > 0:
			s5 = x+s5
			x = 0+9
			x = 8/x
			paths.append(3)
		else:
			s4 = s4+x
			s4 = 1+s4
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))