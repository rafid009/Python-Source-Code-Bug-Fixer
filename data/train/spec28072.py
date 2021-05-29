import numpy as np 

def function(x):

	s9 = 3
	p0 = 1
	x = x
	paths = []
	try:
		if s9 < 1:
			s9 = x-s9
			x = x/4
			paths.append(1)
		else:
			p0 = p0+5
			paths.append(2)
		if s9 > 6:
			p0 = p0/7
			p0 = 8/p0
			x = p0-x
			paths.append(3)
		else:
			s9 = s9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))