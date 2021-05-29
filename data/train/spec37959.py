import numpy as np 

def function(x):

	w9 = x
	m4 = x
	paths = []
	try:
		if x > 8:
			m4 = m4*m4
			m4 = m4-3
			x = x/2
			paths.append(1)
		else:
			x = 4/x
			w9 = w9/x
			paths.append(2)
		if m4 >= 2:
			m4 = m4+2
			m4 = m4+7
			paths.append(3)
		else:
			w9 = 3*w9
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