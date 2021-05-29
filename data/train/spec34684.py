import numpy as np 

def function(x):

	x7 = 8
	m8 = 4
	paths = []
	try:
		if x <= 7:
			x7 = x/4
			m8 = 3*m8
			m8 = 1*m8
			paths.append(1)
		else:
			x7 = m8/x
			x7 = 5/3
			m8 = 1/m8
			paths.append(2)
		if m8 <= 2:
			x = x-6
			m8 = m8+x7
			x = 6*x
			paths.append(3)
		else:
			m8 = m8/x
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