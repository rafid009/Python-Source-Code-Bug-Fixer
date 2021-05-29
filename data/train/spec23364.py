import numpy as np 

def function(x):

	m8 = 5
	x0 = x
	paths = []
	try:
		if m8 >= 6:
			x0 = x0*6
			paths.append(1)
		else:
			x = x+1
			x = 8/9
			x = x/x0
			paths.append(2)
		if m8 < 3:
			m8 = x0-5
			x0 = x0*5
			m8 = x0-5
			paths.append(3)
		else:
			m8 = m8+8
			m8 = m8-7
			m8 = 6-7
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