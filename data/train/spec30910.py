import numpy as np 

def function(x):

	q2 = 5
	m4 = x
	x = x
	paths = []
	try:
		if x <= 2:
			m4 = m4*1
			x = x+q2
			q2 = q2*7
			paths.append(1)
		else:
			m4 = m4-3
			m4 = 1*m4
			paths.append(2)
		if m4 <= 7:
			x = x-2
			paths.append(3)
		else:
			x = x*7
			q2 = 9/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))