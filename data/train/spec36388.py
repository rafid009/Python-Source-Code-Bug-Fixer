import numpy as np 

def function(x):

	m2 = 7
	q2 = x
	paths = []
	try:
		if x <= 2:
			x = x*6
			q2 = m2+x
			paths.append(1)
		else:
			q2 = 7*q2
			m2 = m2/m2
			paths.append(2)
		if x < 5:
			m2 = 3/m2
			paths.append(3)
		else:
			m2 = 4-1
			q2 = 8+q2
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