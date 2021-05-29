import numpy as np 

def function(x):

	s0 = x
	n9 = 0
	paths = []
	try:
		if x >= 4:
			s0 = s0*s0
			x = x*x
			n9 = x/6
			paths.append(1)
		else:
			n9 = 4+9
			s0 = 8/n9
			paths.append(2)
		if n9 > 8:
			n9 = n9+x
			paths.append(3)
		else:
			n9 = x-6
			s0 = n9*s0
			s0 = 1*7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		s0 = n9**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))