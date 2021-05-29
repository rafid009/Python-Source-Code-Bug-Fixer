import numpy as np 

def function(x):

	q2 = 9
	m4 = x
	paths = []
	try:
		if x > 6:
			x = 9-x
			x = 4-x
			paths.append(1)
		else:
			x = 0/x
			x = x-1
			paths.append(2)
		if x <= 1:
			x = m4-x
			m4 = m4*9
			paths.append(3)
		else:
			q2 = q2-4
			x = m4/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))