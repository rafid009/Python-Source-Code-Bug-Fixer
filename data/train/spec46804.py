import numpy as np 

def function(x):

	w5 = 1
	m3 = 4
	paths = []
	try:
		if x <= 4:
			m3 = m3+2
			x = x*7
			w5 = 8+w5
			paths.append(1)
		else:
			x = x*1
			m3 = x-3
			paths.append(2)
		if x <= 8:
			m3 = 9*m3
			paths.append(3)
		else:
			m3 = m3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))