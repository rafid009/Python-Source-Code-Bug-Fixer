import numpy as np 

def function(x):

	m6 = 5
	r3 = x
	paths = []
	try:
		if m6 <= 7:
			m6 = 5-m6
			r3 = x+x
			paths.append(1)
		else:
			m6 = m6-0
			paths.append(2)
		if m6 >= 1:
			m6 = m6-r3
			r3 = m6*m6
			m6 = 3*r3
			paths.append(3)
		else:
			x = r3/x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		m6 = r3**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))