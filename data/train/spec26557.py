import numpy as np 

def function(x):

	m1 = x
	s8 = x
	paths = []
	try:
		if m1 >= 8:
			x = x/1
			s8 = 1/s8
			s8 = s8-m1
			paths.append(1)
		else:
			s8 = s8/8
			s8 = m1+m1
			paths.append(2)
		if s8 >= 5:
			s8 = 8+s8
			x = 0/x
			m1 = 2*x
			paths.append(3)
		else:
			m1 = m1/6
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))