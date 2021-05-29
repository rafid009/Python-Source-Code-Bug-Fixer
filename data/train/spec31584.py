import numpy as np 

def function(x):

	q1 = 3
	m6 = x
	paths = []
	try:
		if m6 <= 8:
			q1 = q1-4
			x = x/1
			x = q1+8
			paths.append(1)
		else:
			q1 = q1+x
			m6 = m6/x
			m6 = q1-m6
			paths.append(2)
		if m6 <= 4:
			m6 = m6/4
			q1 = 5+q1
			x = q1+q1
			paths.append(3)
		else:
			x = x-8
			x = q1+x
			q1 = 4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))