import numpy as np 

def function(x):

	m2 = 0
	u4 = x
	paths = []
	try:
		if x > 3:
			u4 = u4/4
			x = x-x
			paths.append(1)
		else:
			m2 = 0*m2
			paths.append(2)
		if u4 < 0:
			u4 = u4/3
			paths.append(3)
		else:
			m2 = 6-2
			m2 = 9+m2
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