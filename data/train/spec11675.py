import numpy as np 

def function(x):

	q1 = x
	m2 = x
	x = 8
	paths = []
	try:
		if x > 8:
			x = m2+x
			m2 = m2+4
			paths.append(1)
		else:
			q1 = 8/q1
			x = 9/6
			paths.append(2)
		if x > 7:
			m2 = m2+q1
			x = q1/x
			paths.append(3)
		else:
			x = 4/4
			m2 = 0-m2
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		m2 = q1**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))