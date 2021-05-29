import numpy as np 

def function(x):

	q7 = 8
	m2 = 0
	paths = []
	try:
		if q7 > 0:
			m2 = m2*8
			q7 = 3/q7
			paths.append(1)
		else:
			x = 3*4
			q7 = 1+4
			x = 8+x
			paths.append(2)
		if m2 > 3:
			m2 = m2/q7
			q7 = x/9
			q7 = q7+5
			paths.append(3)
		else:
			m2 = m2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))