import numpy as np 

def function(x):

	m0 = x
	e5 = 1
	paths = []
	try:
		if m0 < 1:
			e5 = e5/6
			paths.append(1)
		else:
			e5 = e5+1
			paths.append(2)
		if m0 <= 5:
			e5 = e5-4
			e5 = x-7
			m0 = e5/m0
			paths.append(3)
		else:
			m0 = m0-e5
			m0 = e5+m0
			e5 = e5*e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		m0 = e5**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))