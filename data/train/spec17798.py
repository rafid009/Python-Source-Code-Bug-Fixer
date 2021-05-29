import numpy as np 

def function(x):

	m8 = x
	b2 = 5
	paths = []
	try:
		if b2 < 2:
			b2 = b2+3
			x = 1*x
			b2 = b2+2
			paths.append(1)
		else:
			b2 = 6*b2
			x = 7/x
			paths.append(2)
		if b2 > 7:
			x = x-3
			x = 8-x
			paths.append(3)
		else:
			m8 = 3*m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))