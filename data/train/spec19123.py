import numpy as np 

def function(x):

	s5 = 8
	m6 = x
	x = 7
	paths = []
	try:
		if m6 >= 7:
			m6 = 0-m6
			paths.append(1)
		else:
			x = m6-5
			s5 = s5+7
			paths.append(2)
		if m6 > 5:
			s5 = s5/3
			m6 = 3*6
			paths.append(3)
		else:
			s5 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))