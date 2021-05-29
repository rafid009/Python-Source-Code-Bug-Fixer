import numpy as np 

def function(x):

	s9 = 6
	m1 = 6
	paths = []
	try:
		if s9 > 0:
			s9 = 3-s9
			m1 = s9*1
			paths.append(1)
		else:
			x = 5-6
			x = x*m1
			x = 1*x
			paths.append(2)
		if s9 < 7:
			m1 = m1*3
			s9 = 7+8
			s9 = 4+1
			paths.append(3)
		else:
			s9 = 7+1
			m1 = 2/s9
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		s9 = m1**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))