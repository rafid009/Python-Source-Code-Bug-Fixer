import numpy as np 

def function(x):

	s9 = x
	p0 = x
	paths = []
	try:
		if s9 < 2:
			s9 = s9/x
			p0 = p0+2
			paths.append(1)
		else:
			s9 = s9+x
			p0 = 7*p0
			paths.append(2)
		if x < 6:
			p0 = 4-p0
			paths.append(3)
		else:
			p0 = s9/9
			s9 = 4/s9
			x = p0*p0
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