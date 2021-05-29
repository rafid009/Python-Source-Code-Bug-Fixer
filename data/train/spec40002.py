import numpy as np 

def function(x):

	m6 = 0
	w8 = x
	paths = []
	try:
		if m6 <= 2:
			w8 = x-7
			x = w8+5
			paths.append(1)
		else:
			m6 = m6-2
			w8 = w8-x
			paths.append(2)
		if m6 <= 6:
			x = 9*m6
			w8 = w8*5
			x = x/2
			paths.append(3)
		else:
			x = x/3
			x = m6/5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		m6 = w8**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))