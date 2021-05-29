import numpy as np 

def function(x):

	w4 = 7
	m9 = 3
	paths = []
	try:
		if x > 1:
			w4 = m9-x
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x > 8:
			m9 = m9*1
			paths.append(3)
		else:
			m9 = 1-m9
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		m9 = w4**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))