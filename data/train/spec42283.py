import numpy as np 

def function(x):

	m9 = 7
	m4 = x
	paths = []
	try:
		if x < 3:
			m4 = m9*m4
			m4 = m4/m9
			m9 = m9+8
			paths.append(1)
		else:
			m9 = m4-m9
			m4 = 5*m4
			paths.append(2)
		if m4 > 3:
			m4 = x*m4
			paths.append(3)
		else:
			m4 = m4+3
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m4 = m9**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))