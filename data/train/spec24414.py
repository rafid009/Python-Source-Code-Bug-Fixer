import numpy as np 

def function(x):

	e8 = 1
	m7 = x
	x = 1
	paths = []
	try:
		if e8 > 6:
			x = 2+x
			paths.append(1)
		else:
			m7 = 0-e8
			e8 = 3-e8
			x = x-7
			paths.append(2)
		if e8 > 6:
			e8 = e8/9
			x = 5*9
			paths.append(3)
		else:
			e8 = e8-1
			m7 = m7/m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))