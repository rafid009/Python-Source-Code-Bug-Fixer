import numpy as np 

def function(x):

	m6 = 2
	b0 = 3
	paths = []
	try:
		if m6 < 7:
			m6 = 8*5
			b0 = 7+b0
			paths.append(1)
		else:
			x = 9+4
			m6 = x*m6
			paths.append(2)
		if x > 0:
			b0 = b0+7
			paths.append(3)
		else:
			x = 6*x
			m6 = 1*7
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