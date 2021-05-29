import numpy as np 

def function(x):

	m4 = 5
	q1 = x
	paths = []
	try:
		if q1 < 9:
			m4 = m4/5
			x = x-x
			m4 = 3+m4
			paths.append(1)
		else:
			x = x+2
			m4 = m4/9
			q1 = x/m4
			paths.append(2)
		if x < 9:
			m4 = 0*9
			m4 = m4*q1
			paths.append(3)
		else:
			m4 = 6-m4
			m4 = m4+4
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		m4 = q1**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))