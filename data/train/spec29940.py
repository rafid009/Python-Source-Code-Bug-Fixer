import numpy as np 

def function(x):

	p7 = 1
	s8 = 4
	paths = []
	try:
		if x > 0:
			x = x+x
			x = p7+2
			s8 = s8+6
			paths.append(1)
		else:
			p7 = p7*p7
			paths.append(2)
		if x > 8:
			s8 = x-s8
			p7 = p7-s8
			paths.append(3)
		else:
			p7 = p7-5
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		s8 = p7**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))