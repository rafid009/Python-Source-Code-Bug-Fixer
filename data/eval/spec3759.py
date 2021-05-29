import numpy as np 

def function(x):

	m4 = 5
	s3 = x
	paths = []
	try:
		if m4 < 5:
			x = x*9
			paths.append(1)
		else:
			x = m4+x
			paths.append(2)
		if m4 < 9:
			x = s3-0
			m4 = 3+x
			paths.append(3)
		else:
			x = 2+x
			s3 = x*s3
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		m4 = s3**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))