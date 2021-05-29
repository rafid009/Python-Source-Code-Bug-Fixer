import numpy as np 

def function(x):

	m0 = x
	i9 = 2
	paths = []
	try:
		if m0 > 1:
			i9 = i9*6
			paths.append(1)
		else:
			i9 = i9/m0
			m0 = m0+6
			paths.append(2)
		if m0 >= 7:
			x = x-0
			paths.append(3)
		else:
			m0 = m0-i9
			x = i9/9
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