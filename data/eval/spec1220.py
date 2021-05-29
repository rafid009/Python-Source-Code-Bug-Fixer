import numpy as np 

def function(x):

	m1 = 4
	s3 = x
	paths = []
	try:
		if m1 < 0:
			x = x-m1
			m1 = x*5
			paths.append(1)
		else:
			x = m1/5
			x = x/2
			x = x-7
			paths.append(2)
		if s3 <= 1:
			x = 9/x
			x = m1/2
			x = 9*m1
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		m1 = s3**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))