import numpy as np 

def function(x):

	w8 = x
	m2 = x
	paths = []
	try:
		if w8 <= 6:
			m2 = m2+6
			m2 = 8-m2
			w8 = x-6
			paths.append(1)
		else:
			w8 = w8*9
			paths.append(2)
		if w8 > 3:
			w8 = w8+5
			w8 = 2-w8
			paths.append(3)
		else:
			w8 = 7*3
			m2 = 3-m2
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))