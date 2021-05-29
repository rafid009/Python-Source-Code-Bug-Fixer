import numpy as np 

def function(x):

	u3 = 7
	m6 = 1
	paths = []
	try:
		if m6 < 5:
			x = 5/x
			paths.append(1)
		else:
			m6 = m6-5
			paths.append(2)
		if x <= 3:
			m6 = m6-m6
			paths.append(3)
		else:
			x = x/4
			u3 = 7*u3
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