import numpy as np 

def function(x):

	w0 = 2
	m3 = 0
	paths = []
	try:
		if m3 >= 9:
			m3 = m3/m3
			paths.append(1)
		else:
			m3 = x-5
			x = 4+x
			paths.append(2)
		if m3 >= 2:
			w0 = x*w0
			w0 = 9-w0
			paths.append(3)
		else:
			w0 = w0-9
			x = 9-x
			w0 = 0/m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))