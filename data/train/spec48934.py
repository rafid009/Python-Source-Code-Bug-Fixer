import numpy as np 

def function(x):

	w0 = 0
	m1 = 4
	paths = []
	try:
		if x >= 6:
			w0 = w0-7
			paths.append(1)
		else:
			w0 = w0+7
			paths.append(2)
		if w0 < 6:
			w0 = w0+6
			x = 9-4
			m1 = m1-9
			paths.append(3)
		else:
			x = 6-x
			m1 = m1+4
			w0 = 5/1
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		m1 = w0**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))