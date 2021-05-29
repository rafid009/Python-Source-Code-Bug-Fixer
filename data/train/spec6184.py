import numpy as np 

def function(x):

	m2 = 9
	w8 = 7
	paths = []
	try:
		if m2 >= 6:
			x = x/2
			paths.append(1)
		else:
			w8 = m2+w8
			paths.append(2)
		if w8 > 8:
			w8 = w8-w8
			x = m2/x
			m2 = 3+m2
			paths.append(3)
		else:
			w8 = 9*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))