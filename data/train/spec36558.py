import numpy as np 

def function(x):

	y8 = x
	m8 = 8
	paths = []
	try:
		if y8 >= 0:
			m8 = 1-m8
			y8 = 2*y8
			paths.append(1)
		else:
			x = m8*4
			m8 = 2+m8
			paths.append(2)
		if x > 6:
			y8 = y8+m8
			x = 0-9
			paths.append(3)
		else:
			x = x+3
			m8 = x*m8
			m8 = x-7
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))