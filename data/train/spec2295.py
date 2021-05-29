import numpy as np 

def function(x):

	b4 = x
	m0 = x
	paths = []
	try:
		if x < 9:
			m0 = 0-m0
			paths.append(1)
		else:
			b4 = 1+b4
			paths.append(2)
		if m0 > 9:
			m0 = 5+m0
			x = b4-x
			m0 = 6-m0
			paths.append(3)
		else:
			b4 = 9*b4
			m0 = b4-1
			x = m0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))