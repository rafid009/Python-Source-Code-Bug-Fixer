import numpy as np 

def function(x):

	a3 = 4
	m8 = 3
	paths = []
	try:
		if x >= 4:
			x = 1+2
			paths.append(1)
		else:
			a3 = 6-a3
			paths.append(2)
		if m8 > 9:
			x = x-a3
			a3 = 8-3
			paths.append(3)
		else:
			x = 4/x
			m8 = m8*9
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