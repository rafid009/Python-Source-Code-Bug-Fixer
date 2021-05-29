import numpy as np 

def function(x):

	m9 = x
	x0 = 8
	paths = []
	try:
		if m9 >= 4:
			m9 = m9-4
			x = m9-9
			m9 = m9-4
			paths.append(1)
		else:
			x0 = 1*m9
			x0 = x*5
			x0 = 3/x0
			paths.append(2)
		if x0 > 9:
			m9 = x0+4
			paths.append(3)
		else:
			x0 = 7-x0
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