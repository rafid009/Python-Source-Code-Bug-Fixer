import numpy as np 

def function(x):

	y7 = 3
	m4 = x
	paths = []
	try:
		if m4 <= 5:
			x = x*2
			paths.append(1)
		else:
			m4 = m4/y7
			y7 = 0-y7
			paths.append(2)
		if y7 < 6:
			m4 = 3/m4
			paths.append(3)
		else:
			m4 = 7-1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))