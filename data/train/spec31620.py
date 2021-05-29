import numpy as np 

def function(x):

	m6 = 7
	w1 = 0
	paths = []
	try:
		if m6 > 9:
			x = 5*x
			w1 = 0-7
			x = 9+x
			paths.append(1)
		else:
			w1 = w1-9
			m6 = m6-7
			m6 = 5+m6
			paths.append(2)
		if w1 > 9:
			w1 = w1-3
			m6 = m6+1
			w1 = w1-w1
			paths.append(3)
		else:
			m6 = x/5
			x = x/7
			x = w1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))