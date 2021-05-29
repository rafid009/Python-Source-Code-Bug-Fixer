import numpy as np 

def function(x):

	i8 = 8
	m0 = x
	paths = []
	try:
		if m0 < 2:
			i8 = 6*x
			i8 = 7/i8
			paths.append(1)
		else:
			x = 3-x
			m0 = m0+2
			m0 = 2+8
			paths.append(2)
		if i8 >= 6:
			m0 = 1+x
			i8 = i8+x
			paths.append(3)
		else:
			i8 = i8-i8
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