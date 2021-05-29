import numpy as np 

def function(x):

	m8 = 6
	y4 = 6
	x = 6
	paths = []
	try:
		if x < 4:
			y4 = x-8
			paths.append(1)
		else:
			x = x-m8
			x = 9-6
			m8 = 0-m8
			paths.append(2)
		if m8 >= 8:
			m8 = 9*7
			y4 = y4*3
			y4 = 7/y4
			paths.append(3)
		else:
			x = x-6
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))