import numpy as np 

def function(x):

	m0 = 1
	v3 = 3
	paths = []
	try:
		if x >= 9:
			v3 = v3+9
			paths.append(1)
		else:
			m0 = m0-4
			x = x/8
			x = x-8
			paths.append(2)
		if m0 < 1:
			x = x-x
			paths.append(3)
		else:
			x = x-5
			v3 = v3/v3
			x = 8*6
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))