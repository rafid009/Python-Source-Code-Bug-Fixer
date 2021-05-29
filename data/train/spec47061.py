import numpy as np 

def function(x):

	m1 = 1
	s3 = 0
	paths = []
	try:
		if x >= 5:
			m1 = 2*m1
			s3 = s3/m1
			paths.append(1)
		else:
			m1 = x+m1
			m1 = m1-3
			m1 = 8+m1
			paths.append(2)
		if m1 > 0:
			m1 = m1+s3
			s3 = s3*7
			x = x/8
			paths.append(3)
		else:
			s3 = s3/9
			s3 = s3-1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		s3 = m1**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))