import numpy as np 

def function(x):

	m2 = x
	a3 = 8
	paths = []
	try:
		if m2 > 1:
			a3 = a3-8
			m2 = m2-x
			paths.append(1)
		else:
			m2 = m2/7
			a3 = x-a3
			paths.append(2)
		if a3 >= 2:
			x = 4*4
			x = m2/1
			x = m2/7
			paths.append(3)
		else:
			a3 = a3*a3
			a3 = 7-x
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