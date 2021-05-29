import numpy as np 

def function(x):

	w4 = 3
	m5 = x
	paths = []
	try:
		if m5 < 2:
			x = 6/x
			x = w4+x
			paths.append(1)
		else:
			w4 = 6+w4
			w4 = w4*1
			paths.append(2)
		if x < 5:
			m5 = m5/4
			x = 1-8
			w4 = 0+w4
			paths.append(3)
		else:
			x = m5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))