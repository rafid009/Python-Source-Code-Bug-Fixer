import numpy as np 

def function(x):

	m9 = 8
	s2 = x
	paths = []
	try:
		if x > 3:
			x = 3-x
			s2 = s2/4
			x = x/7
			paths.append(1)
		else:
			m9 = x*m9
			paths.append(2)
		if s2 > 0:
			s2 = x*x
			paths.append(3)
		else:
			x = x-m9
			s2 = s2-m9
			x = 0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))