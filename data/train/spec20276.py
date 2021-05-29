import numpy as np 

def function(x):

	s8 = x
	j3 = x
	paths = []
	try:
		if s8 < 8:
			j3 = 1+j3
			x = j3-x
			paths.append(1)
		else:
			j3 = 3-j3
			x = 4+1
			paths.append(2)
		if s8 <= 9:
			s8 = s8/2
			j3 = j3/2
			x = 4/x
			paths.append(3)
		else:
			s8 = s8-2
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))