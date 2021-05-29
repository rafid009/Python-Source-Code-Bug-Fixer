import numpy as np 

def function(x):

	m8 = x
	y2 = x
	paths = []
	try:
		if y2 >= 0:
			y2 = m8-2
			x = 3+x
			paths.append(1)
		else:
			x = 9+7
			x = x/1
			m8 = 3+m8
			paths.append(2)
		if x <= 9:
			m8 = 3-2
			paths.append(3)
		else:
			m8 = m8+m8
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))