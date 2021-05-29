import numpy as np 

def function(x):

	s6 = 3
	m9 = x
	paths = []
	try:
		if s6 > 4:
			m9 = 8+5
			paths.append(1)
		else:
			m9 = m9+9
			m9 = m9/6
			s6 = 1/1
			paths.append(2)
		if x <= 0:
			m9 = 6+4
			x = x*7
			m9 = m9/3
			paths.append(3)
		else:
			s6 = s6-2
			s6 = 5/1
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))