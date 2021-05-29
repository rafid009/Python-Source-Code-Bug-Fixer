import numpy as np 

def function(x):

	m2 = x
	m9 = x
	paths = []
	try:
		if m2 < 4:
			x = x-7
			m9 = m9+x
			m2 = 0*m2
			paths.append(1)
		else:
			x = 4/8
			m9 = 9-m9
			x = 4+x
			paths.append(2)
		if x >= 9:
			x = 3+3
			m9 = x/m9
			m9 = 9*m2
			paths.append(3)
		else:
			x = 1+6
			m2 = 4-m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))