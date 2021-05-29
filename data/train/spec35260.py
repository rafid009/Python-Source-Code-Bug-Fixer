import numpy as np 

def function(x):

	m1 = x
	u8 = 1
	paths = []
	try:
		if x < 9:
			x = x-6
			paths.append(1)
		else:
			m1 = 8+6
			paths.append(2)
		if x < 5:
			x = x+6
			u8 = x/u8
			paths.append(3)
		else:
			u8 = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))