import numpy as np 

def function(x):

	b1 = x
	m0 = 9
	paths = []
	try:
		if m0 <= 8:
			b1 = b1/m0
			paths.append(1)
		else:
			x = 1-9
			paths.append(2)
		if b1 > 5:
			x = 0-7
			x = 8/x
			paths.append(3)
		else:
			m0 = 5/m0
			x = m0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))