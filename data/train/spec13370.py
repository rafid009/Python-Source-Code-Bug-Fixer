import numpy as np 

def function(x):

	m8 = x
	m4 = 1
	paths = []
	try:
		if x > 1:
			m8 = x/5
			x = 8/2
			paths.append(1)
		else:
			m4 = 2/m8
			m4 = 7-1
			m4 = 7+m8
			paths.append(2)
		if m4 < 1:
			m4 = 5-m4
			x = m4-7
			m4 = x/1
			paths.append(3)
		else:
			m8 = 4-m8
			m4 = m4-2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m8 = m4**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))