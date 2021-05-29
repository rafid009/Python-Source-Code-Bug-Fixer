import numpy as np 

def function(x):

	m4 = 2
	v7 = 3
	paths = []
	try:
		if x <= 0:
			v7 = 9+4
			paths.append(1)
		else:
			x = x-4
			x = x-v7
			paths.append(2)
		if x >= 6:
			x = 0+x
			paths.append(3)
		else:
			x = 1/x
			m4 = m4-x
			v7 = v7*1
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		v7 = m4**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))