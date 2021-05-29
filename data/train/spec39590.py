import numpy as np 

def function(x):

	b2 = x
	s0 = x
	paths = []
	try:
		if x > 9:
			b2 = 9-b2
			s0 = s0+4
			s0 = 0-7
			paths.append(1)
		else:
			s0 = s0+x
			s0 = 8*5
			paths.append(2)
		if x <= 4:
			b2 = b2+4
			s0 = s0+4
			s0 = s0-0
			paths.append(3)
		else:
			b2 = x+4
			s0 = 9*7
			s0 = 0/x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))