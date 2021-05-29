import numpy as np 

def function(x):

	m1 = x
	l5 = 8
	paths = []
	try:
		if m1 > 2:
			m1 = 4/2
			paths.append(1)
		else:
			l5 = l5/6
			paths.append(2)
		if m1 >= 3:
			x = 1-x
			m1 = 9+x
			paths.append(3)
		else:
			m1 = 3*4
			m1 = 6-m1
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