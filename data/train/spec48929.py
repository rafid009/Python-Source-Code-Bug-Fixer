import numpy as np 

def function(x):

	m0 = 0
	l7 = 5
	paths = []
	try:
		if l7 >= 2:
			m0 = m0+7
			paths.append(1)
		else:
			m0 = 2*m0
			l7 = l7-6
			l7 = x*3
			paths.append(2)
		if m0 > 4:
			l7 = x+9
			x = 9-x
			paths.append(3)
		else:
			l7 = 1+x
			l7 = x+l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))