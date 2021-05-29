import numpy as np 

def function(x):

	u8 = 9
	m0 = 1
	paths = []
	try:
		if x <= 9:
			u8 = 1-u8
			u8 = 0-u8
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if m0 > 1:
			u8 = u8+8
			paths.append(3)
		else:
			m0 = m0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))