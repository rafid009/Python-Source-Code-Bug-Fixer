import numpy as np 

def function(x):

	m3 = x
	s3 = x
	paths = []
	try:
		if x <= 7:
			x = x/x
			paths.append(1)
		else:
			s3 = x*4
			paths.append(2)
		if s3 < 6:
			x = m3*x
			m3 = m3*5
			m3 = m3*2
			paths.append(3)
		else:
			x = 3*x
			m3 = 0/m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		s3 = m3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))