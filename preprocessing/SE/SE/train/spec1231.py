import numpy as np 

def function(x):

	a5 = x
	m4 = x
	paths = []
	try:
		if x >= 4:
			x = m4-x
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if m4 > 6:
			x = x*a5
			paths.append(3)
		else:
			m4 = m4/6
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