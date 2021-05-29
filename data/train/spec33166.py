import numpy as np 

def function(x):

	q2 = x
	m9 = 5
	paths = []
	try:
		if m9 <= 2:
			q2 = q2/6
			m9 = m9+2
			paths.append(1)
		else:
			q2 = 7*6
			paths.append(2)
		if x >= 1:
			x = x+q2
			m9 = 0*m9
			m9 = x+m9
			paths.append(3)
		else:
			q2 = 8-8
			m9 = 4*8
			x = 9*x
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