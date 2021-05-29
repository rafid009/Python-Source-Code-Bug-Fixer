import numpy as np 

def function(x):

	p4 = 0
	s2 = 4
	x = 8
	paths = []
	try:
		if s2 <= 0:
			p4 = p4*p4
			paths.append(1)
		else:
			s2 = s2-5
			p4 = p4-8
			p4 = 7+x
			paths.append(2)
		if s2 < 2:
			s2 = 4/s2
			p4 = s2+p4
			paths.append(3)
		else:
			x = p4/7
			s2 = 8-8
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))