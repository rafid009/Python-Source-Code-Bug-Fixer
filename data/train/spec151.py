import numpy as np 

def function(x):

	s8 = 2
	m7 = 6
	paths = []
	try:
		if m7 > 3:
			s8 = s8-m7
			m7 = m7+2
			x = x+8
			paths.append(1)
		else:
			x = x*m7
			paths.append(2)
		if m7 <= 9:
			x = x+m7
			paths.append(3)
		else:
			x = x-6
			m7 = x+5
			x = s8/x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		m7 = s8**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))