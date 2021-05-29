import numpy as np 

def function(x):

	m4 = x
	w5 = 3
	paths = []
	try:
		if x <= 2:
			x = 0+x
			w5 = w5/w5
			x = x+5
			paths.append(1)
		else:
			x = 6+x
			x = 6*w5
			paths.append(2)
		if x > 3:
			x = x+6
			paths.append(3)
		else:
			w5 = 2*w5
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))