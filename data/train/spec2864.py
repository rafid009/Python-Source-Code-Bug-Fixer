import numpy as np 

def function(x):

	m7 = x
	s3 = 8
	paths = []
	try:
		if x < 0:
			s3 = 9*s3
			paths.append(1)
		else:
			s3 = 7*s3
			m7 = x*1
			paths.append(2)
		if m7 >= 7:
			m7 = 4+m7
			paths.append(3)
		else:
			m7 = m7*1
			m7 = m7*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))