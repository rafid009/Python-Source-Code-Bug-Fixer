import numpy as np 

def function(x):

	n8 = 5
	s6 = x
	paths = []
	try:
		if n8 < 2:
			s6 = 1-s6
			n8 = 2/n8
			s6 = n8/5
			paths.append(1)
		else:
			s6 = 7*s6
			x = x/4
			n8 = 4*s6
			paths.append(2)
		if s6 > 8:
			s6 = s6+2
			x = x-s6
			paths.append(3)
		else:
			n8 = 3-x
			s6 = s6+n8
			x = x/4
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		n8 = s6**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))