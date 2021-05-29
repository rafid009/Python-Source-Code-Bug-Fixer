import numpy as np 

def function(x):

	s5 = 9
	p2 = x
	paths = []
	try:
		if x > 1:
			p2 = p2-s5
			s5 = 3-0
			paths.append(1)
		else:
			p2 = s5+8
			paths.append(2)
		if x > 1:
			x = 7/x
			s5 = s5+3
			paths.append(3)
		else:
			s5 = s5/8
			s5 = x-s5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		s5 = p2**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))