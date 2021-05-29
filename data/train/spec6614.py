import numpy as np 

def function(x):

	b0 = 8
	m6 = 6
	paths = []
	try:
		if m6 < 6:
			m6 = m6/m6
			b0 = 6/b0
			x = x*9
			paths.append(1)
		else:
			m6 = 5/m6
			paths.append(2)
		if x > 6:
			x = m6-x
			paths.append(3)
		else:
			b0 = b0*m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))