import numpy as np 

def function(x):

	m0 = 6
	a5 = x
	x = x
	paths = []
	try:
		if a5 > 1:
			a5 = a5-5
			paths.append(1)
		else:
			m0 = m0+a5
			a5 = a5*a5
			paths.append(2)
		if x >= 2:
			m0 = x-1
			m0 = x-m0
			a5 = a5-2
			paths.append(3)
		else:
			x = x-m0
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		m0 = a5**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))