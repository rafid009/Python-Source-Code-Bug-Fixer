import numpy as np 

def function(x):

	y3 = x
	m8 = x
	paths = []
	try:
		if m8 < 2:
			x = 9*x
			paths.append(1)
		else:
			y3 = 2-y3
			paths.append(2)
		if y3 >= 1:
			x = x-x
			y3 = 2-3
			m8 = m8-7
			paths.append(3)
		else:
			m8 = m8*2
			m8 = m8/m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))