import numpy as np 

def function(x):

	e4 = 6
	m3 = 3
	paths = []
	try:
		if m3 <= 6:
			x = 7-1
			x = x/1
			paths.append(1)
		else:
			e4 = 7*1
			paths.append(2)
		if e4 <= 8:
			m3 = m3+e4
			m3 = 0-4
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))