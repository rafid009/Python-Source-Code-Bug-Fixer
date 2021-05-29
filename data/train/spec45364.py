import numpy as np 

def function(x):

	m2 = x
	x0 = 1
	paths = []
	try:
		if x < 4:
			x0 = x0+x
			paths.append(1)
		else:
			x0 = 8-x0
			x0 = x-4
			x0 = x0+m2
			paths.append(2)
		if m2 > 9:
			x = 6*x
			paths.append(3)
		else:
			x0 = 3-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))