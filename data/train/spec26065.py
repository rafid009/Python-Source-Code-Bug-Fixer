import numpy as np 

def function(x):

	m5 = x
	m7 = x
	paths = []
	try:
		if m7 <= 1:
			m5 = m5+0
			m7 = 9-m7
			m7 = 0*m5
			paths.append(1)
		else:
			m7 = m7+m5
			paths.append(2)
		if x <= 8:
			m7 = m7*m5
			paths.append(3)
		else:
			x = x-0
			m7 = m7/m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))