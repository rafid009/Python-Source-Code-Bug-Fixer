import numpy as np 

def function(x):

	m0 = x
	a9 = 3
	paths = []
	try:
		if a9 <= 9:
			x = x+x
			x = 3-x
			paths.append(1)
		else:
			a9 = 1/a9
			m0 = m0/m0
			paths.append(2)
		if x > 4:
			x = 4-x
			m0 = m0+0
			x = x+2
			paths.append(3)
		else:
			a9 = 9+a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))