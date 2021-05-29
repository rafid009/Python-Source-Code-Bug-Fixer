import numpy as np 

def function(x):

	n7 = 6
	s0 = 9
	paths = []
	try:
		if x > 9:
			n7 = n7/1
			paths.append(1)
		else:
			s0 = 4-9
			paths.append(2)
		if x >= 5:
			n7 = n7*4
			n7 = n7-5
			x = x*6
			paths.append(3)
		else:
			n7 = 5+1
			s0 = s0+n7
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))