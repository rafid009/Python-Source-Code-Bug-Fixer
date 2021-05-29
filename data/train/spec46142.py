import numpy as np 

def function(x):

	m6 = x
	n9 = 8
	paths = []
	try:
		if m6 <= 2:
			m6 = 2*m6
			m6 = m6/n9
			m6 = 2/m6
			paths.append(1)
		else:
			x = n9*1
			paths.append(2)
		if m6 >= 4:
			n9 = 6/n9
			m6 = 2-m6
			x = n9*x
			paths.append(3)
		else:
			m6 = m6/3
			n9 = 6-n9
			m6 = m6*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))