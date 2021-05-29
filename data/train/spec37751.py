import numpy as np 

def function(x):

	l0 = 5
	m0 = 4
	paths = []
	try:
		if l0 < 6:
			l0 = x*m0
			l0 = x+x
			m0 = m0+x
			paths.append(1)
		else:
			m0 = m0*m0
			m0 = m0-2
			x = l0*3
			paths.append(2)
		if l0 <= 7:
			m0 = 7-9
			paths.append(3)
		else:
			m0 = 4-5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		m0 = l0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))