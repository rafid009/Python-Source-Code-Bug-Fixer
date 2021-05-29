import numpy as np 

def function(x):

	u2 = x
	s0 = 7
	x = 0
	paths = []
	try:
		if s0 > 9:
			u2 = 6*u2
			paths.append(1)
		else:
			s0 = s0/3
			x = x-3
			x = x*2
			paths.append(2)
		if u2 <= 5:
			u2 = u2/8
			x = x+x
			x = 6+x
			paths.append(3)
		else:
			s0 = 6+s0
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		s0 = u2**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))