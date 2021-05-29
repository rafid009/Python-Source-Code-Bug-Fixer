import numpy as np 

def function(x):

	m1 = 4
	s5 = x
	paths = []
	try:
		if s5 <= 7:
			m1 = 0/4
			x = x-m1
			m1 = 6*m1
			paths.append(1)
		else:
			x = 1/3
			s5 = 6+s5
			s5 = s5/8
			paths.append(2)
		if x <= 2:
			s5 = s5+9
			paths.append(3)
		else:
			m1 = 1/x
			x = x/1
			x = x/s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))