import numpy as np 

def function(x):

	m6 = x
	w3 = 8
	paths = []
	try:
		if x > 2:
			w3 = w3-9
			x = x/1
			paths.append(1)
		else:
			m6 = w3-2
			m6 = x+2
			paths.append(2)
		if w3 < 8:
			x = 3*m6
			paths.append(3)
		else:
			x = x+m6
			m6 = m6/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))