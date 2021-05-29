import numpy as np 

def function(x):

	m6 = 6
	p7 = 6
	x = x
	paths = []
	try:
		if x < 1:
			p7 = p7-4
			paths.append(1)
		else:
			m6 = m6-p7
			m6 = m6+4
			paths.append(2)
		if p7 >= 4:
			p7 = x-p7
			paths.append(3)
		else:
			p7 = x/2
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