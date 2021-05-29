import numpy as np 

def function(x):

	w9 = x
	m8 = x
	paths = []
	try:
		if m8 < 2:
			m8 = 9/m8
			m8 = 2*7
			paths.append(1)
		else:
			m8 = 3-m8
			w9 = m8+5
			paths.append(2)
		if w9 > 1:
			m8 = x+m8
			m8 = m8-m8
			paths.append(3)
		else:
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		w9 = m8**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))