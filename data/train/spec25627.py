import numpy as np 

def function(x):

	s5 = 2
	p7 = x
	paths = []
	try:
		if p7 < 6:
			x = 7-s5
			x = s5/x
			p7 = 1+p7
			paths.append(1)
		else:
			s5 = x*s5
			s5 = s5*8
			paths.append(2)
		if s5 > 9:
			s5 = s5*4
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		s5 = p7**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))