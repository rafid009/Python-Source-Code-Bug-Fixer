import numpy as np 

def function(x):

	m7 = x
	y7 = x
	paths = []
	try:
		if y7 < 3:
			x = 5*x
			x = 0+x
			paths.append(1)
		else:
			y7 = y7-6
			paths.append(2)
		if y7 >= 5:
			m7 = m7*8
			paths.append(3)
		else:
			m7 = m7-4
			m7 = m7/y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))