import numpy as np 

def function(x):

	m8 = x
	l8 = 4
	paths = []
	try:
		if x <= 2:
			m8 = m8+9
			l8 = 4-8
			paths.append(1)
		else:
			m8 = 2+m8
			paths.append(2)
		if l8 > 7:
			x = x-0
			l8 = l8*4
			l8 = 1+l8
			paths.append(3)
		else:
			m8 = 3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))