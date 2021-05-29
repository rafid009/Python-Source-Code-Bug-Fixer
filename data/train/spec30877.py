import numpy as np 

def function(x):

	p0 = 8
	s6 = x
	paths = []
	try:
		if s6 > 0:
			p0 = s6/p0
			p0 = 8/p0
			paths.append(1)
		else:
			x = 6/3
			p0 = x+p0
			x = x-6
			paths.append(2)
		if p0 > 5:
			x = x-6
			x = x/p0
			paths.append(3)
		else:
			x = 3/x
			p0 = 6+p0
			s6 = p0/s6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))