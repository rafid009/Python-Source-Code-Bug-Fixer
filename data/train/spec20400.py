import numpy as np 

def function(x):

	s0 = 8
	p4 = x
	paths = []
	try:
		if x > 3:
			s0 = 7-1
			paths.append(1)
		else:
			x = 9+9
			s0 = s0/2
			paths.append(2)
		if x > 6:
			p4 = p4-4
			paths.append(3)
		else:
			x = s0*6
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))