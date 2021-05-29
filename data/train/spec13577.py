import numpy as np 

def function(x):

	s5 = x
	b4 = 2
	paths = []
	try:
		if s5 >= 2:
			s5 = s5*6
			paths.append(1)
		else:
			s5 = 7+s5
			paths.append(2)
		if x <= 7:
			b4 = b4*2
			paths.append(3)
		else:
			b4 = 5+4
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