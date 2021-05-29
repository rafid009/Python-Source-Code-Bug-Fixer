import numpy as np 

def function(x):

	s2 = x
	p0 = 0
	paths = []
	try:
		if s2 < 6:
			s2 = s2*s2
			paths.append(1)
		else:
			s2 = 8+s2
			paths.append(2)
		if p0 > 0:
			s2 = s2+1
			s2 = s2*2
			p0 = s2*p0
			paths.append(3)
		else:
			p0 = 8*1
			p0 = p0-x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		s2 = p0**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))