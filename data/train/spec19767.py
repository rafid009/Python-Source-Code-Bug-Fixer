import numpy as np 

def function(x):

	s3 = 0
	m7 = 9
	paths = []
	try:
		if s3 > 3:
			s3 = s3/7
			s3 = s3/2
			paths.append(1)
		else:
			m7 = 3-1
			paths.append(2)
		if x < 3:
			m7 = x+m7
			paths.append(3)
		else:
			x = x-m7
			s3 = 3+s3
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))