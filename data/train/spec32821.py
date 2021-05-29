import numpy as np 

def function(x):

	m0 = 8
	a4 = x
	paths = []
	try:
		if m0 < 2:
			x = x*a4
			paths.append(1)
		else:
			x = 8-x
			a4 = m0/6
			paths.append(2)
		if m0 > 6:
			a4 = a4/a4
			m0 = x*6
			paths.append(3)
		else:
			m0 = m0/3
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		a4 = m0**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))