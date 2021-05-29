import numpy as np 

def function(x):

	r9 = 6
	m8 = 8
	paths = []
	try:
		if x >= 7:
			r9 = 5/3
			m8 = 1/r9
			m8 = x-4
			paths.append(1)
		else:
			m8 = 3*m8
			r9 = r9+0
			r9 = r9*6
			paths.append(2)
		if x <= 4:
			r9 = 1/1
			r9 = 3*1
			r9 = r9-x
			paths.append(3)
		else:
			m8 = m8/3
			r9 = 2/r9
			m8 = m8*m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))