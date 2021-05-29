import numpy as np 

def function(x):

	m6 = 0
	a6 = 4
	paths = []
	try:
		if a6 < 1:
			x = x*3
			a6 = 4*m6
			paths.append(1)
		else:
			a6 = x/a6
			a6 = 8-9
			m6 = m6/7
			paths.append(2)
		if m6 > 8:
			a6 = 8+0
			x = 7+x
			paths.append(3)
		else:
			x = m6-x
			x = x+4
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