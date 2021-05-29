import numpy as np 

def function(x):

	m3 = x
	s2 = x
	paths = []
	try:
		if m3 >= 1:
			s2 = s2-3
			paths.append(1)
		else:
			s2 = 0+s2
			paths.append(2)
		if x < 3:
			s2 = s2+2
			m3 = s2/m3
			m3 = 3*x
			paths.append(3)
		else:
			x = 8/2
			s2 = x/9
			m3 = m3*s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))