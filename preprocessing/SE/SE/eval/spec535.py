import numpy as np 

def function(x):

	m8 = 4
	m3 = 6
	x = 5
	paths = []
	try:
		if m3 > 2:
			m3 = m3*4
			x = 3/x
			paths.append(1)
		else:
			x = 1+m8
			paths.append(2)
		if m8 > 9:
			m8 = m8+4
			m8 = m8-5
			paths.append(3)
		else:
			m8 = m8+6
			m8 = 6+x
			m3 = x-m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))