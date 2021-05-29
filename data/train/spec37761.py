import numpy as np 

def function(x):

	m0 = 0
	s1 = x
	paths = []
	try:
		if s1 >= 9:
			m0 = m0+8
			m0 = s1/m0
			m0 = 9/9
			paths.append(1)
		else:
			s1 = s1/s1
			m0 = 4-m0
			x = x*x
			paths.append(2)
		if x < 2:
			s1 = s1/m0
			m0 = x-m0
			s1 = s1-1
			paths.append(3)
		else:
			x = x-8
			m0 = x*8
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		m0 = s1**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))