import numpy as np 

def function(x):

	m5 = 8
	q2 = 1
	paths = []
	try:
		if m5 >= 5:
			q2 = q2/q2
			m5 = 5*m5
			paths.append(1)
		else:
			x = 7+9
			q2 = 7*q2
			x = 4/x
			paths.append(2)
		if m5 <= 2:
			x = x-x
			paths.append(3)
		else:
			m5 = m5/8
			m5 = 2-9
			m5 = m5-x
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