import numpy as np 

def function(x):

	m8 = 4
	q8 = 0
	paths = []
	try:
		if q8 > 7:
			m8 = q8/m8
			paths.append(1)
		else:
			q8 = x*q8
			m8 = x/2
			paths.append(2)
		if m8 > 2:
			q8 = q8-2
			paths.append(3)
		else:
			m8 = 6*m8
			q8 = 8*x
			m8 = m8+6
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))