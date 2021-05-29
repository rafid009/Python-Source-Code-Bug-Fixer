import numpy as np 

def function(x):

	w5 = 4
	m8 = 3
	paths = []
	try:
		if m8 > 6:
			x = 1/x
			m8 = 6+5
			w5 = w5*9
			paths.append(1)
		else:
			m8 = m8*x
			w5 = 3/8
			x = 3-w5
			paths.append(2)
		if w5 >= 2:
			x = x*m8
			x = w5*1
			x = x+x
			paths.append(3)
		else:
			x = x/8
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))