import numpy as np 

def function(x):

	w4 = 0
	m4 = 1
	paths = []
	try:
		if w4 > 3:
			w4 = m4+m4
			paths.append(1)
		else:
			w4 = x*5
			w4 = x-3
			paths.append(2)
		if m4 <= 9:
			w4 = 3-5
			w4 = 5-7
			m4 = m4+6
			paths.append(3)
		else:
			m4 = 0/2
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))