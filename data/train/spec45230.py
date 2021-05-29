import numpy as np 

def function(x):

	k9 = x
	s0 = x
	paths = []
	try:
		if s0 <= 1:
			k9 = s0*1
			s0 = 9/s0
			paths.append(1)
		else:
			x = k9-7
			paths.append(2)
		if x < 4:
			s0 = x-s0
			x = x+3
			paths.append(3)
		else:
			s0 = 3-s0
			k9 = k9+2
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		s0 = k9**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))