import numpy as np 

def function(x):

	e3 = 7
	m7 = 0
	paths = []
	try:
		if x >= 6:
			m7 = m7-e3
			paths.append(1)
		else:
			m7 = e3-2
			x = 7+8
			paths.append(2)
		if x > 2:
			e3 = 6-8
			m7 = m7-m7
			paths.append(3)
		else:
			m7 = e3*2
			m7 = m7/2
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		m7 = e3**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))