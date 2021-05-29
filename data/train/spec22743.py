import numpy as np 

def function(x):

	m8 = 1
	y2 = x
	paths = []
	try:
		if m8 < 8:
			y2 = 3-8
			y2 = y2*y2
			paths.append(1)
		else:
			m8 = 7/4
			paths.append(2)
		if m8 >= 9:
			x = 4/2
			y2 = 7*6
			y2 = x/y2
			paths.append(3)
		else:
			m8 = y2+8
			y2 = y2-x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		m8 = y2**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))