import numpy as np 

def function(x):

	m4 = 8
	n6 = x
	paths = []
	try:
		if n6 < 2:
			x = m4/1
			x = 3/7
			m4 = 9-m4
			paths.append(1)
		else:
			n6 = x-6
			n6 = 7+n6
			x = 4-x
			paths.append(2)
		if m4 >= 9:
			x = 4*m4
			paths.append(3)
		else:
			m4 = 4*m4
			x = n6*x
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