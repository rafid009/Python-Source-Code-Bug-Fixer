import numpy as np 

def function(x):

	m4 = x
	s6 = 2
	paths = []
	try:
		if x >= 2:
			x = 0-x
			paths.append(1)
		else:
			m4 = m4*8
			x = x*0
			paths.append(2)
		if m4 < 3:
			m4 = 6*m4
			s6 = 0+s6
			x = x+5
			paths.append(3)
		else:
			m4 = m4/8
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))