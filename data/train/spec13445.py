import numpy as np 

def function(x):

	a7 = 1
	m0 = 3
	paths = []
	try:
		if a7 <= 9:
			x = 8*x
			a7 = 1-3
			paths.append(1)
		else:
			m0 = a7-5
			x = 5+x
			x = 9*x
			paths.append(2)
		if m0 < 1:
			m0 = 4+m0
			paths.append(3)
		else:
			a7 = a7-9
			m0 = 6/3
			a7 = a7*4
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		m0 = a7**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))