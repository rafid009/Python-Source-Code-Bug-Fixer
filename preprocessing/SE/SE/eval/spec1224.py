import numpy as np 

def function(x):

	m6 = 2
	w1 = x
	paths = []
	try:
		if m6 <= 6:
			x = x+8
			m6 = m6/m6
			paths.append(1)
		else:
			w1 = x-1
			w1 = 9*w1
			paths.append(2)
		if x <= 3:
			w1 = w1+3
			paths.append(3)
		else:
			m6 = m6+x
			m6 = 2*w1
			w1 = w1*w1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))