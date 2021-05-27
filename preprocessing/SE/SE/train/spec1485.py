import numpy as np 

def function(x):

	m9 = x
	q0 = x
	paths = []
	try:
		if m9 <= 0:
			m9 = m9+6
			x = x/2
			m9 = 2-m9
			paths.append(1)
		else:
			x = q0+x
			q0 = q0*8
			paths.append(2)
		if m9 > 3:
			q0 = 5*q0
			paths.append(3)
		else:
			q0 = 1*x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		q0 = m9**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))