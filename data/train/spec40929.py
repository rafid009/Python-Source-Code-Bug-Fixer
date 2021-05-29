import numpy as np 

def function(x):

	m7 = 6
	s5 = 8
	paths = []
	try:
		if m7 < 3:
			x = m7*7
			m7 = 8-m7
			s5 = s5-2
			paths.append(1)
		else:
			m7 = 1+x
			s5 = 3+x
			s5 = 4/m7
			paths.append(2)
		if m7 >= 8:
			m7 = m7*m7
			s5 = m7/2
			paths.append(3)
		else:
			m7 = 1-m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))