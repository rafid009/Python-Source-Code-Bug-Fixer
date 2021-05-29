import numpy as np 

def function(x):

	s0 = 6
	p1 = 3
	paths = []
	try:
		if s0 < 7:
			s0 = s0/x
			p1 = 5/s0
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if p1 < 8:
			p1 = 9+p1
			paths.append(3)
		else:
			x = 9+x
			x = 1/1
			p1 = s0/x
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