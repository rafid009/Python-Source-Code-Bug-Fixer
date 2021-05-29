import numpy as np 

def function(x):

	p2 = x
	s8 = 4
	x = 4
	paths = []
	try:
		if s8 > 6:
			p2 = p2-1
			paths.append(1)
		else:
			s8 = x*s8
			x = 6-1
			s8 = s8/s8
			paths.append(2)
		if s8 >= 5:
			p2 = p2+1
			s8 = p2/x
			s8 = s8/x
			paths.append(3)
		else:
			x = x/5
			p2 = p2*6
			s8 = s8-8
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		s8 = p2**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))