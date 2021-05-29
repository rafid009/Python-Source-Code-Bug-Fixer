import numpy as np 

def function(x):

	m6 = x
	q1 = 8
	x = x
	paths = []
	try:
		if q1 < 1:
			q1 = q1-3
			m6 = m6+m6
			paths.append(1)
		else:
			m6 = m6-8
			q1 = 9-8
			paths.append(2)
		if m6 >= 6:
			x = 6-q1
			q1 = q1+5
			x = x/3
			paths.append(3)
		else:
			m6 = m6+q1
			x = x+0
			x = x-4
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