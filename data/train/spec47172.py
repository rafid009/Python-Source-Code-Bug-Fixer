import numpy as np 

def function(x):

	p0 = 8
	s6 = 6
	x = 9
	paths = []
	try:
		if p0 >= 2:
			x = x+7
			paths.append(1)
		else:
			s6 = p0/1
			s6 = s6*s6
			s6 = s6-2
			paths.append(2)
		if p0 < 9:
			s6 = x-s6
			x = 6-x
			paths.append(3)
		else:
			x = 7-x
			p0 = p0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))