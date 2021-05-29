import numpy as np 

def function(x):

	s6 = 1
	p7 = 1
	paths = []
	try:
		if p7 >= 7:
			p7 = p7*1
			x = x-p7
			paths.append(1)
		else:
			p7 = x-8
			s6 = x-s6
			paths.append(2)
		if s6 < 6:
			s6 = s6-p7
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))