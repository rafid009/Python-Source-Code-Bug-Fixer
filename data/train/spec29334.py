import numpy as np 

def function(x):

	m8 = x
	y7 = x
	paths = []
	try:
		if y7 > 9:
			x = 1-x
			m8 = 4+3
			y7 = 6-m8
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if y7 >= 2:
			m8 = m8+0
			y7 = 2+y7
			m8 = 5-8
			paths.append(3)
		else:
			x = m8-x
			m8 = m8*1
			y7 = x-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		m8 = y7**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))