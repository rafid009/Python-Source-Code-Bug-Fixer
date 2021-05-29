import numpy as np 

def function(x):

	s0 = 0
	n1 = 7
	paths = []
	try:
		if x >= 1:
			x = 5/3
			x = 8+s0
			paths.append(1)
		else:
			n1 = 9/n1
			n1 = n1+4
			s0 = s0/n1
			paths.append(2)
		if s0 >= 5:
			x = 9+x
			n1 = 3/n1
			x = s0/9
			paths.append(3)
		else:
			n1 = 6-n1
			n1 = s0+x
			x = x+s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))