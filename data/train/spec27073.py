import numpy as np 

def function(x):

	y8 = x
	m3 = x
	paths = []
	try:
		if y8 >= 1:
			x = m3+0
			y8 = m3+3
			m3 = m3+4
			paths.append(1)
		else:
			m3 = m3/y8
			paths.append(2)
		if x > 5:
			m3 = m3-2
			paths.append(3)
		else:
			m3 = m3+2
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