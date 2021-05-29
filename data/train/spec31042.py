import numpy as np 

def function(x):

	m4 = 7
	w2 = x
	x = x
	paths = []
	try:
		if w2 <= 0:
			w2 = 8/w2
			m4 = m4/6
			m4 = m4/5
			paths.append(1)
		else:
			m4 = x+6
			m4 = 0-x
			paths.append(2)
		if w2 < 6:
			x = w2-8
			w2 = 2-w2
			x = x-0
			paths.append(3)
		else:
			m4 = m4+4
			w2 = m4*w2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))