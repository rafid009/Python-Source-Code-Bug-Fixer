import numpy as np 

def function(x):

	s3 = 5
	m1 = 6
	paths = []
	try:
		if s3 < 1:
			m1 = 7+m1
			paths.append(1)
		else:
			s3 = s3+8
			m1 = m1/m1
			paths.append(2)
		if m1 > 6:
			s3 = s3*m1
			s3 = s3-3
			paths.append(3)
		else:
			m1 = 5+s3
			s3 = x+m1
			m1 = 1+9
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))