import numpy as np 

def function(x):

	s4 = 3
	p6 = 9
	paths = []
	try:
		if s4 <= 1:
			s4 = 3+9
			paths.append(1)
		else:
			p6 = x+p6
			p6 = 1-6
			p6 = s4*8
			paths.append(2)
		if x >= 0:
			p6 = 4-p6
			x = 2/8
			s4 = 3/s4
			paths.append(3)
		else:
			x = 4+x
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))