import numpy as np 

def function(x):

	t8 = 2
	m8 = 1
	paths = []
	try:
		if x < 3:
			t8 = 1*4
			m8 = 8+m8
			paths.append(1)
		else:
			x = x-x
			x = t8-x
			paths.append(2)
		if x >= 3:
			x = 2/x
			paths.append(3)
		else:
			t8 = t8*1
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