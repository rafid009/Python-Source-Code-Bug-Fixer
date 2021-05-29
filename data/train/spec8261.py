import numpy as np 

def function(x):

	w8 = x
	m4 = x
	paths = []
	try:
		if w8 <= 1:
			m4 = 0/5
			x = 8-2
			x = x-5
			paths.append(1)
		else:
			w8 = w8-0
			m4 = 0-m4
			m4 = 3+m4
			paths.append(2)
		if m4 < 9:
			w8 = 6*w8
			m4 = m4-5
			paths.append(3)
		else:
			w8 = 9+m4
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