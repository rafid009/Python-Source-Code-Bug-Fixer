import numpy as np 

def function(x):

	m4 = 5
	q0 = 3
	paths = []
	try:
		if q0 <= 1:
			x = x/2
			q0 = q0/q0
			paths.append(1)
		else:
			q0 = q0*x
			x = 9+8
			paths.append(2)
		if m4 < 7:
			m4 = 8+m4
			x = m4+2
			q0 = q0-m4
			paths.append(3)
		else:
			m4 = m4*6
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))