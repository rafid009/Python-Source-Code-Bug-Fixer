import numpy as np 

def function(x):

	y1 = 1
	m7 = 8
	x = 6
	paths = []
	try:
		if y1 > 8:
			y1 = 5/y1
			x = 2-x
			m7 = x+4
			paths.append(1)
		else:
			y1 = 7*6
			paths.append(2)
		if y1 >= 2:
			m7 = 1-m7
			x = 5/x
			paths.append(3)
		else:
			x = y1-m7
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))