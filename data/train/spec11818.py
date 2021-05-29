import numpy as np 

def function(x):

	p7 = 5
	m6 = 1
	x = x
	paths = []
	try:
		if p7 <= 8:
			m6 = 8/p7
			m6 = 6-2
			paths.append(1)
		else:
			x = 2*9
			paths.append(2)
		if x <= 3:
			m6 = m6-p7
			m6 = p7/m6
			m6 = 3+m6
			paths.append(3)
		else:
			x = x-1
			m6 = 3+m6
			m6 = m6-2
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