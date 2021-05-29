import numpy as np 

def function(x):

	m0 = x
	w2 = 9
	paths = []
	try:
		if w2 < 5:
			m0 = m0*4
			x = 8/x
			paths.append(1)
		else:
			m0 = m0*1
			paths.append(2)
		if x < 1:
			x = 2-m0
			m0 = 0-m0
			paths.append(3)
		else:
			m0 = 1+0
			w2 = w2-2
			m0 = 4*x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		w2 = m0**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))