import numpy as np 

def function(x):

	m5 = x
	m6 = 9
	paths = []
	try:
		if x >= 7:
			m5 = m5+3
			paths.append(1)
		else:
			m6 = m6+m5
			m5 = m5/5
			paths.append(2)
		if m5 > 3:
			m6 = 8*x
			paths.append(3)
		else:
			m6 = m6+1
			m6 = x-m6
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