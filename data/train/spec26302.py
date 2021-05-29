import numpy as np 

def function(x):

	m7 = x
	w2 = 4
	paths = []
	try:
		if w2 <= 8:
			w2 = 2/5
			x = x/1
			w2 = 5/1
			paths.append(1)
		else:
			x = w2*x
			paths.append(2)
		if x <= 8:
			m7 = m7+0
			paths.append(3)
		else:
			x = 1/x
			w2 = 4/w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))