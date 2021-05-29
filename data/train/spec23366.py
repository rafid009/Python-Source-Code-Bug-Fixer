import numpy as np 

def function(x):

	m4 = 5
	x1 = 6
	paths = []
	try:
		if m4 >= 0:
			x = 5/x
			x = x1/x
			x1 = 0-x1
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if m4 > 0:
			x = 6*x
			paths.append(3)
		else:
			m4 = m4*9
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))