import numpy as np 

def function(x):

	s5 = x
	s0 = 2
	x = 7
	paths = []
	try:
		if s0 > 9:
			s5 = 9/s5
			s0 = x+6
			paths.append(1)
		else:
			x = s5+s5
			paths.append(2)
		if x < 7:
			s5 = s5-3
			paths.append(3)
		else:
			s5 = s5/s0
			x = x*2
			x = x/8
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