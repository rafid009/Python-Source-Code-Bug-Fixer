import numpy as np 

def function(x):

	s8 = 9
	m9 = x
	paths = []
	try:
		if m9 <= 9:
			x = x-x
			s8 = s8-3
			m9 = m9+s8
			paths.append(1)
		else:
			s8 = s8/m9
			paths.append(2)
		if s8 > 4:
			s8 = m9*1
			paths.append(3)
		else:
			s8 = m9-m9
			s8 = 6-s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		m9 = s8**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))