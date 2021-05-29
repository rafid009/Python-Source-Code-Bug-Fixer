import numpy as np 

def function(x):

	q0 = x
	m5 = 4
	paths = []
	try:
		if q0 <= 7:
			q0 = q0*7
			q0 = 6/8
			paths.append(1)
		else:
			x = 2+q0
			paths.append(2)
		if q0 <= 1:
			m5 = m5+x
			paths.append(3)
		else:
			q0 = q0+q0
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))