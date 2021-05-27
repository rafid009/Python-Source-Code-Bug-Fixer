import numpy as np 

def function(x):

	m8 = x
	w3 = x
	paths = []
	try:
		if w3 > 4:
			m8 = m8-w3
			m8 = 5*3
			m8 = m8/1
			paths.append(1)
		else:
			w3 = 5+w3
			paths.append(2)
		if w3 <= 4:
			x = 9*m8
			m8 = m8-4
			paths.append(3)
		else:
			x = m8*1
			w3 = 3*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))