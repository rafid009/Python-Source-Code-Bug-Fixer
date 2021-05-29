import numpy as np 

def function(x):

	a5 = 2
	m2 = 0
	paths = []
	try:
		if a5 <= 0:
			a5 = a5/a5
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if m2 < 3:
			m2 = 5-9
			paths.append(3)
		else:
			a5 = 9-a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))