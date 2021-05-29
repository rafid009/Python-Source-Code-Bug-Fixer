import numpy as np 

def function(x):

	p8 = x
	s2 = 9
	paths = []
	try:
		if s2 < 8:
			x = 2*8
			paths.append(1)
		else:
			p8 = s2+p8
			paths.append(2)
		if p8 >= 9:
			p8 = 4/p8
			s2 = 2*s2
			p8 = x+p8
			paths.append(3)
		else:
			x = p8-8
			s2 = s2*x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		p8 = s2**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))