import numpy as np 

def function(x):

	l7 = 5
	m0 = x
	paths = []
	try:
		if l7 < 6:
			m0 = 1/8
			x = m0+x
			x = m0/x
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if m0 >= 7:
			l7 = m0/m0
			l7 = 1+l7
			m0 = m0+0
			paths.append(3)
		else:
			m0 = 4*m0
			l7 = l7-1
			m0 = 7-m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))