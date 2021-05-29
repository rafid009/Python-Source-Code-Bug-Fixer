import numpy as np 

def function(x):

	w8 = 1
	m6 = x
	paths = []
	try:
		if m6 < 8:
			m6 = m6/9
			paths.append(1)
		else:
			w8 = w8*1
			w8 = x/w8
			x = x/m6
			paths.append(2)
		if m6 >= 5:
			m6 = 6*4
			m6 = x/m6
			paths.append(3)
		else:
			x = x/6
			x = 6/x
			w8 = w8-7
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