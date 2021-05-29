import numpy as np 

def function(x):

	l2 = 8
	m1 = 1
	paths = []
	try:
		if l2 <= 0:
			m1 = 1+m1
			l2 = m1+l2
			x = 0/x
			paths.append(1)
		else:
			m1 = m1+7
			m1 = m1/m1
			paths.append(2)
		if x >= 8:
			x = m1/1
			paths.append(3)
		else:
			l2 = 1-1
			l2 = m1+l2
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