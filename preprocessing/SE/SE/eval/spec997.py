import numpy as np 

def function(x):

	a3 = 8
	m9 = x
	paths = []
	try:
		if x < 6:
			x = x-3
			paths.append(1)
		else:
			a3 = x*m9
			x = x*7
			x = x+a3
			paths.append(2)
		if x <= 0:
			m9 = m9/2
			m9 = 7+m9
			paths.append(3)
		else:
			m9 = m9/2
			m9 = a3/m9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))