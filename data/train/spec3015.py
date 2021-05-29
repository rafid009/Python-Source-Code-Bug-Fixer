import numpy as np 

def function(x):

	m6 = x
	y7 = x
	x = 6
	paths = []
	try:
		if y7 > 8:
			m6 = 0*m6
			m6 = m6-0
			paths.append(1)
		else:
			y7 = m6-y7
			paths.append(2)
		if y7 < 4:
			x = x-x
			y7 = m6-9
			paths.append(3)
		else:
			x = y7+4
			y7 = x*9
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		m6 = y7**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))