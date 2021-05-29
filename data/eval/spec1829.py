import numpy as np 

def function(x):

	b2 = x
	m4 = x
	paths = []
	try:
		if m4 < 3:
			x = x-5
			b2 = x*m4
			paths.append(1)
		else:
			m4 = m4-x
			b2 = 9-5
			paths.append(2)
		if b2 > 7:
			m4 = 3*x
			b2 = 8-b2
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))