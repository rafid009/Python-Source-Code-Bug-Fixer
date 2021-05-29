import numpy as np 

def function(x):

	m4 = 5
	q3 = 8
	paths = []
	try:
		if x <= 8:
			q3 = 1*1
			q3 = m4/x
			paths.append(1)
		else:
			m4 = x/m4
			q3 = 5/6
			paths.append(2)
		if q3 > 6:
			m4 = m4-x
			x = x-x
			paths.append(3)
		else:
			q3 = 9/q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		m4 = q3**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))