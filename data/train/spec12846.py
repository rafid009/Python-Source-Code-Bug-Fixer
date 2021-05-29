import numpy as np 

def function(x):

	m2 = x
	l2 = x
	paths = []
	try:
		if l2 <= 2:
			l2 = l2+8
			x = l2+x
			m2 = m2*4
			paths.append(1)
		else:
			l2 = x-l2
			x = 0/x
			paths.append(2)
		if l2 > 5:
			m2 = m2-m2
			paths.append(3)
		else:
			m2 = m2/9
			l2 = 7*l2
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))