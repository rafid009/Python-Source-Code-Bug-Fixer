import numpy as np 

def function(x):

	y4 = x
	m1 = 4
	paths = []
	try:
		if m1 < 2:
			m1 = m1+5
			paths.append(1)
		else:
			m1 = 8/y4
			m1 = x-m1
			paths.append(2)
		if y4 >= 5:
			y4 = 1/y4
			paths.append(3)
		else:
			m1 = m1*4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		m1 = y4**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))