import numpy as np 

def function(x):

	y3 = x
	m3 = x
	paths = []
	try:
		if x <= 4:
			y3 = 9*y3
			m3 = m3*4
			paths.append(1)
		else:
			m3 = m3*9
			m3 = m3/x
			m3 = m3/y3
			paths.append(2)
		if m3 >= 7:
			y3 = 9-y3
			paths.append(3)
		else:
			y3 = 2+y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		m3 = y3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))