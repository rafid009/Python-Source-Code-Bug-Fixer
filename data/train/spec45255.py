import numpy as np 

def function(x):

	m9 = x
	s3 = x
	paths = []
	try:
		if s3 > 3:
			m9 = 6*4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if s3 < 4:
			s3 = s3-3
			paths.append(3)
		else:
			m9 = m9*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))