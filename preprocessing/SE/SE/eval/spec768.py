import numpy as np 

def function(x):

	m1 = x
	q7 = x
	x = 7
	paths = []
	try:
		if q7 > 1:
			m1 = m1*m1
			q7 = 2+q7
			paths.append(1)
		else:
			m1 = m1/6
			q7 = q7/1
			paths.append(2)
		if m1 <= 8:
			x = x/x
			q7 = q7-3
			x = 1/m1
			paths.append(3)
		else:
			m1 = m1+3
			q7 = 9-q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		m1 = q7**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))