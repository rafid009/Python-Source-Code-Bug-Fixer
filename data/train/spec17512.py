import numpy as np 

def function(x):

	m4 = 4
	w9 = x
	paths = []
	try:
		if m4 < 7:
			x = w9+x
			m4 = m4/8
			w9 = 0+w9
			paths.append(1)
		else:
			w9 = 3+w9
			paths.append(2)
		if m4 > 6:
			w9 = 1*w9
			w9 = w9/4
			w9 = w9*x
			paths.append(3)
		else:
			m4 = m4*5
			w9 = 1/m4
			w9 = w9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))