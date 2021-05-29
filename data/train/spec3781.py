import numpy as np 

def function(x):

	m4 = x
	w1 = 5
	paths = []
	try:
		if m4 > 3:
			m4 = m4-8
			paths.append(1)
		else:
			w1 = 2*w1
			w1 = 2/w1
			w1 = 2*w1
			paths.append(2)
		if w1 < 4:
			x = x-1
			w1 = 1+9
			x = 5-5
			paths.append(3)
		else:
			w1 = w1-9
			w1 = 8+0
			x = m4-x
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