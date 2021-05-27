import numpy as np 

def function(x):

	w2 = 9
	m8 = x
	paths = []
	try:
		if w2 >= 4:
			m8 = 6-m8
			m8 = 2*m8
			x = 3-x
			paths.append(1)
		else:
			x = 1-1
			paths.append(2)
		if m8 < 0:
			w2 = 0*4
			m8 = 0*x
			w2 = w2+8
			paths.append(3)
		else:
			x = m8*x
			m8 = 7+m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))