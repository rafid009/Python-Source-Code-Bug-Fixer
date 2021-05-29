import numpy as np 

def function(x):

	m2 = 9
	y8 = 1
	paths = []
	try:
		if x <= 0:
			y8 = 1-7
			m2 = m2/m2
			paths.append(1)
		else:
			m2 = x-y8
			paths.append(2)
		if y8 > 5:
			y8 = y8+1
			x = 4-x
			paths.append(3)
		else:
			m2 = 8-4
			m2 = 7+m2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))