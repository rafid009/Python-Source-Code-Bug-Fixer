import numpy as np 

def function(x):

	m6 = 0
	l7 = x
	paths = []
	try:
		if l7 > 9:
			m6 = m6+5
			paths.append(1)
		else:
			l7 = l7/1
			m6 = 6*x
			x = x+8
			paths.append(2)
		if l7 >= 3:
			m6 = 9-4
			paths.append(3)
		else:
			m6 = m6*m6
			m6 = m6-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))