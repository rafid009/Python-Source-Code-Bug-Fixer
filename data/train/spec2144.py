import numpy as np 

def function(x):

	m7 = 8
	s2 = x
	paths = []
	try:
		if m7 <= 1:
			x = 4-x
			x = x-8
			s2 = s2/5
			paths.append(1)
		else:
			x = s2-2
			m7 = 9*m7
			paths.append(2)
		if s2 >= 3:
			m7 = 1*m7
			s2 = s2-s2
			paths.append(3)
		else:
			m7 = m7+7
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))