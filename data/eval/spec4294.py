import numpy as np 

def function(x):

	m9 = x
	r9 = 2
	paths = []
	try:
		if x > 5:
			x = 2/x
			paths.append(1)
		else:
			x = m9+x
			x = 6/x
			paths.append(2)
		if r9 <= 7:
			m9 = m9/m9
			m9 = r9*9
			paths.append(3)
		else:
			r9 = 6-3
			r9 = 2/m9
			r9 = r9/r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))