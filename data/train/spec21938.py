import numpy as np 

def function(x):

	m8 = 1
	x2 = 1
	paths = []
	try:
		if m8 > 1:
			x2 = x-m8
			x2 = 6/4
			paths.append(1)
		else:
			m8 = m8*x2
			x2 = 1+m8
			paths.append(2)
		if m8 >= 8:
			x = 5-m8
			paths.append(3)
		else:
			m8 = m8-2
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