import numpy as np 

def function(x):

	s4 = x
	s0 = x
	paths = []
	try:
		if s0 > 5:
			s0 = 0*s0
			s0 = 6*s0
			paths.append(1)
		else:
			x = x+s4
			paths.append(2)
		if s4 <= 7:
			s4 = s4*8
			x = 5+7
			s0 = s4*x
			paths.append(3)
		else:
			s0 = x+s0
			x = s0+s0
			s4 = s4*x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))