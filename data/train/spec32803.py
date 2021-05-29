import numpy as np 

def function(x):

	m1 = 6
	q5 = x
	paths = []
	try:
		if x < 2:
			x = x-q5
			paths.append(1)
		else:
			x = 9/x
			x = q5-x
			paths.append(2)
		if q5 >= 8:
			x = q5-x
			x = x-q5
			paths.append(3)
		else:
			q5 = m1*3
			m1 = 1+m1
			q5 = m1*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))