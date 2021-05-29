import numpy as np 

def function(x):

	p8 = x
	s0 = 4
	paths = []
	try:
		if p8 <= 0:
			p8 = p8/9
			s0 = 4-8
			s0 = 3-s0
			paths.append(1)
		else:
			s0 = 8/6
			paths.append(2)
		if p8 <= 4:
			s0 = p8-s0
			paths.append(3)
		else:
			p8 = p8+9
			p8 = p8/p8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))