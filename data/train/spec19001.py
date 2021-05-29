import numpy as np 

def function(x):

	z5 = x
	m1 = 0
	x = 1
	paths = []
	try:
		if x <= 1:
			x = 8-1
			paths.append(1)
		else:
			m1 = 9-m1
			m1 = m1+6
			paths.append(2)
		if x > 5:
			x = x+0
			paths.append(3)
		else:
			z5 = 7-8
			x = x-x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		m1 = z5**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))