import numpy as np 

def function(x):

	m2 = 2
	w9 = x
	paths = []
	try:
		if x > 5:
			m2 = m2-w9
			paths.append(1)
		else:
			w9 = x/x
			w9 = w9-x
			paths.append(2)
		if w9 <= 1:
			m2 = x/6
			paths.append(3)
		else:
			m2 = m2*w9
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