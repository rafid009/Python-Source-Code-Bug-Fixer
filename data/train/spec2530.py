import numpy as np 

def function(x):

	s0 = x
	p8 = 4
	paths = []
	try:
		if s0 >= 9:
			s0 = 2+7
			paths.append(1)
		else:
			p8 = p8/2
			p8 = p8-s0
			s0 = s0/2
			paths.append(2)
		if s0 < 7:
			x = x+6
			x = 6-s0
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))