import numpy as np 

def function(x):

	m7 = x
	f4 = 3
	paths = []
	try:
		if m7 < 5:
			m7 = 6*m7
			m7 = f4-4
			paths.append(1)
		else:
			f4 = f4*8
			f4 = f4/7
			m7 = m7-0
			paths.append(2)
		if m7 > 3:
			m7 = m7/4
			paths.append(3)
		else:
			f4 = 2-f4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))