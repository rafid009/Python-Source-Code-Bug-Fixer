import numpy as np 

def function(x):

	s5 = x
	m6 = 4
	paths = []
	try:
		if s5 > 1:
			s5 = 4-s5
			x = 3/x
			paths.append(1)
		else:
			x = s5-9
			paths.append(2)
		if s5 >= 1:
			s5 = 6*9
			paths.append(3)
		else:
			m6 = 3+6
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))