import numpy as np 

def function(x):

	m6 = 3
	j4 = x
	paths = []
	try:
		if x >= 6:
			x = x-0
			j4 = 6+j4
			j4 = 0+4
			paths.append(1)
		else:
			x = x+9
			j4 = j4-7
			j4 = m6/6
			paths.append(2)
		if m6 >= 0:
			j4 = 0/j4
			paths.append(3)
		else:
			x = 8+8
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