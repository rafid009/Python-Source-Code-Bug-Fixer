import numpy as np 

def function(x):

	s5 = 7
	m1 = x
	paths = []
	try:
		if s5 > 3:
			s5 = s5/7
			m1 = m1*6
			paths.append(1)
		else:
			x = x+3
			x = 5/x
			paths.append(2)
		if s5 >= 1:
			x = 8+4
			paths.append(3)
		else:
			s5 = 7+s5
			m1 = m1-x
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		s5 = m1**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))