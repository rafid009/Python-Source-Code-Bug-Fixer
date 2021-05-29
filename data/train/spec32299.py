import numpy as np 

def function(x):

	m0 = x
	w7 = x
	paths = []
	try:
		if x <= 1:
			m0 = m0-w7
			w7 = w7-x
			paths.append(1)
		else:
			m0 = w7-x
			w7 = 1+w7
			paths.append(2)
		if m0 >= 5:
			m0 = m0*4
			w7 = w7*1
			w7 = 6+w7
			paths.append(3)
		else:
			w7 = w7*8
			m0 = 1+9
			m0 = 0-4
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))