import numpy as np 

def function(x):

	a2 = x
	m0 = 0
	paths = []
	try:
		if m0 >= 6:
			x = 8/a2
			x = x-7
			m0 = 6/a2
			paths.append(1)
		else:
			a2 = a2*a2
			paths.append(2)
		if a2 > 3:
			a2 = m0+a2
			x = x/7
			a2 = 3*a2
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))