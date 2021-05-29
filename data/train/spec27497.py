import numpy as np 

def function(x):

	k7 = 9
	s6 = 8
	paths = []
	try:
		if s6 < 7:
			s6 = s6+1
			s6 = 9*s6
			paths.append(1)
		else:
			s6 = 1-s6
			paths.append(2)
		if x < 8:
			k7 = 0+k7
			s6 = 5/s6
			k7 = 2-1
			paths.append(3)
		else:
			s6 = s6/2
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		k7 = s6**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))