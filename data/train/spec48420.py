import numpy as np 

def function(x):

	q1 = 1
	m9 = x
	paths = []
	try:
		if m9 >= 8:
			q1 = 1*q1
			q1 = q1/1
			q1 = 0+x
			paths.append(1)
		else:
			q1 = x*q1
			paths.append(2)
		if m9 > 7:
			m9 = m9/x
			paths.append(3)
		else:
			q1 = 3*8
			m9 = 3-x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))