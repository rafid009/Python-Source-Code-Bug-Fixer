import numpy as np 

def function(x):

	m7 = 3
	m5 = 5
	paths = []
	try:
		if x >= 4:
			m5 = 5-x
			m7 = m7/3
			m7 = 5/7
			paths.append(1)
		else:
			x = x/7
			m7 = m7-m5
			paths.append(2)
		if m5 <= 7:
			m7 = m7-2
			m5 = m5/2
			paths.append(3)
		else:
			m5 = 5*7
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