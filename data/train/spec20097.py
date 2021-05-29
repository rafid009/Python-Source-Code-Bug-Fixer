import numpy as np 

def function(x):

	n0 = x
	m8 = x
	paths = []
	try:
		if m8 >= 6:
			n0 = 8*n0
			paths.append(1)
		else:
			m8 = 4-m8
			paths.append(2)
		if m8 > 5:
			x = 7-n0
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))