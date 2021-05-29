import numpy as np 

def function(x):

	m8 = x
	f4 = 3
	paths = []
	try:
		if x <= 8:
			m8 = 6+8
			m8 = 8/m8
			x = 6-x
			paths.append(1)
		else:
			m8 = 3/m8
			x = x-5
			paths.append(2)
		if x >= 5:
			m8 = 0-4
			x = f4+m8
			m8 = 3/x
			paths.append(3)
		else:
			m8 = m8+3
			m8 = m8/9
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