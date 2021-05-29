import numpy as np 

def function(x):

	s7 = x
	m1 = 3
	x = 2
	paths = []
	try:
		if x <= 8:
			m1 = 9/m1
			paths.append(1)
		else:
			x = 3+s7
			m1 = 0-m1
			paths.append(2)
		if x < 4:
			x = s7-0
			s7 = m1+9
			paths.append(3)
		else:
			x = 7/x
			s7 = s7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))