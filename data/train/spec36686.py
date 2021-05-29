import numpy as np 

def function(x):

	u4 = x
	m1 = 5
	paths = []
	try:
		if m1 > 2:
			m1 = 1/m1
			u4 = u4+6
			paths.append(1)
		else:
			m1 = m1+3
			paths.append(2)
		if m1 > 5:
			x = x-6
			u4 = u4+u4
			paths.append(3)
		else:
			u4 = 1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))