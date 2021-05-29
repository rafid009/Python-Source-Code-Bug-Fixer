import numpy as np 

def function(x):

	m1 = 8
	s1 = 6
	paths = []
	try:
		if s1 <= 9:
			x = 3+x
			paths.append(1)
		else:
			s1 = 9-3
			s1 = 6+s1
			paths.append(2)
		if s1 >= 7:
			x = 8-x
			s1 = 7*5
			x = 2-x
			paths.append(3)
		else:
			m1 = 2-m1
			s1 = s1*m1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))