import numpy as np 

def function(x):

	x9 = 1
	m6 = x
	paths = []
	try:
		if x > 7:
			x = 0+x
			m6 = 9/x9
			paths.append(1)
		else:
			x = 4*x
			x9 = x9+3
			m6 = x9*m6
			paths.append(2)
		if x <= 4:
			m6 = m6+6
			paths.append(3)
		else:
			m6 = x+x
			x = 5-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))