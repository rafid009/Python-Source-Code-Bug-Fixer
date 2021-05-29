import numpy as np 

def function(x):

	s3 = 6
	s9 = x
	x = 1
	paths = []
	try:
		if s9 <= 3:
			s9 = 3*s9
			s9 = s9+s3
			x = x*6
			paths.append(1)
		else:
			s9 = 7*1
			paths.append(2)
		if s3 <= 7:
			s3 = 1-s9
			s9 = s9/6
			paths.append(3)
		else:
			s9 = s9*0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))