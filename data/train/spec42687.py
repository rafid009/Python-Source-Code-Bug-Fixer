import numpy as np 

def function(x):

	m0 = 9
	a8 = x
	x = x
	paths = []
	try:
		if x >= 2:
			a8 = m0/a8
			paths.append(1)
		else:
			m0 = 2/a8
			paths.append(2)
		if a8 > 9:
			a8 = a8/5
			paths.append(3)
		else:
			a8 = 6-9
			a8 = a8*x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))