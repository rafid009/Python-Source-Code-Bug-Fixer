import numpy as np 

def function(x):

	l0 = 0
	m0 = 1
	paths = []
	try:
		if l0 < 4:
			m0 = m0+l0
			m0 = m0+m0
			paths.append(1)
		else:
			m0 = 5*8
			x = x-4
			m0 = 3/4
			paths.append(2)
		if x >= 6:
			m0 = m0-8
			m0 = x/m0
			l0 = l0-5
			paths.append(3)
		else:
			l0 = l0-l0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))