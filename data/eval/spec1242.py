import numpy as np 

def function(x):

	m9 = x
	w3 = 8
	paths = []
	try:
		if w3 <= 3:
			x = w3-2
			w3 = w3*4
			w3 = 2*w3
			paths.append(1)
		else:
			w3 = x-w3
			w3 = w3-3
			paths.append(2)
		if w3 >= 3:
			w3 = w3-m9
			w3 = 0+8
			paths.append(3)
		else:
			w3 = w3/x
			x = 9/5
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))