import numpy as np 

def function(x):

	m3 = x
	q6 = 1
	paths = []
	try:
		if q6 > 0:
			q6 = 7+x
			x = q6/x
			paths.append(1)
		else:
			q6 = q6*6
			m3 = q6-3
			paths.append(2)
		if m3 >= 6:
			m3 = 1*m3
			q6 = 9*7
			paths.append(3)
		else:
			q6 = m3-q6
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))