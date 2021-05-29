import numpy as np 

def function(x):

	j9 = 2
	m8 = 3
	paths = []
	try:
		if x < 3:
			j9 = 8/x
			x = x-2
			paths.append(1)
		else:
			m8 = 7+m8
			x = x+7
			paths.append(2)
		if x < 6:
			j9 = j9+m8
			m8 = 2/m8
			m8 = x/6
			paths.append(3)
		else:
			j9 = m8+j9
			j9 = j9*x
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