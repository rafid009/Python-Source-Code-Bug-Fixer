import numpy as np 

def function(x):

	k7 = x
	s6 = 7
	paths = []
	try:
		if k7 > 2:
			s6 = s6/8
			s6 = 1*s6
			k7 = k7/3
			paths.append(1)
		else:
			x = x*3
			x = 6-x
			paths.append(2)
		if k7 > 6:
			s6 = 2+s6
			x = 3/8
			s6 = 5-s6
			paths.append(3)
		else:
			x = x-k7
			s6 = s6-4
			x = x-1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))