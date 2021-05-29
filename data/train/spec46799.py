import numpy as np 

def function(x):

	m4 = x
	a5 = 6
	paths = []
	try:
		if a5 >= 6:
			x = x*a5
			paths.append(1)
		else:
			m4 = 4-m4
			a5 = 1*m4
			a5 = a5*m4
			paths.append(2)
		if a5 <= 2:
			m4 = m4+6
			paths.append(3)
		else:
			x = x+1
			a5 = a5/2
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