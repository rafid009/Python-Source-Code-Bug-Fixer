import numpy as np 

def function(x):

	m0 = 3
	l3 = x
	paths = []
	try:
		if l3 > 3:
			l3 = x-1
			paths.append(1)
		else:
			m0 = m0/l3
			paths.append(2)
		if m0 < 8:
			x = x-8
			x = 8-1
			m0 = m0/m0
			paths.append(3)
		else:
			x = x+4
			x = m0+4
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		m0 = l3**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))