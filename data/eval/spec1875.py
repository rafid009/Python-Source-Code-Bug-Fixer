import numpy as np 

def function(x):

	p6 = 6
	s0 = 3
	paths = []
	try:
		if s0 <= 5:
			x = x+x
			x = s0*p6
			paths.append(1)
		else:
			p6 = p6+s0
			s0 = s0+3
			x = 4+3
			paths.append(2)
		if s0 < 0:
			s0 = s0/9
			p6 = 9-p6
			paths.append(3)
		else:
			s0 = s0-7
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))