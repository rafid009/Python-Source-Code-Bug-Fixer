import numpy as np 

def function(x):

	a9 = 5
	m8 = x
	x = 0
	paths = []
	try:
		if x > 0:
			a9 = 0/m8
			paths.append(1)
		else:
			a9 = 4-a9
			a9 = m8/m8
			x = x-m8
			paths.append(2)
		if m8 > 8:
			a9 = a9+a9
			paths.append(3)
		else:
			m8 = m8*m8
			m8 = m8/2
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