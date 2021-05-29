import numpy as np 

def function(x):

	m3 = x
	q3 = x
	paths = []
	try:
		if q3 >= 1:
			x = 1-x
			paths.append(1)
		else:
			m3 = 3-m3
			m3 = m3/6
			m3 = m3*x
			paths.append(2)
		if m3 <= 0:
			q3 = q3+8
			paths.append(3)
		else:
			q3 = m3-q3
			m3 = m3*0
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		q3 = m3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))