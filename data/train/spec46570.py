import numpy as np 

def function(x):

	m4 = x
	s4 = 5
	paths = []
	try:
		if m4 < 3:
			m4 = 1*m4
			x = s4-x
			paths.append(1)
		else:
			s4 = 7*0
			m4 = x/m4
			paths.append(2)
		if x < 8:
			m4 = m4-3
			m4 = m4-1
			s4 = s4-6
			paths.append(3)
		else:
			s4 = m4+x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))