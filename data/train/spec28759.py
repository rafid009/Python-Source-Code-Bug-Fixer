import numpy as np 

def function(x):

	w9 = 4
	m8 = x
	paths = []
	try:
		if x > 6:
			w9 = 3*x
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if x >= 6:
			x = x/w9
			paths.append(3)
		else:
			w9 = 0*w9
			x = x-8
			w9 = w9+w9
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))