import numpy as np 

def function(x):

	m3 = x
	q2 = 8
	paths = []
	try:
		if m3 >= 1:
			x = 9+x
			paths.append(1)
		else:
			q2 = 7/q2
			q2 = m3+5
			paths.append(2)
		if q2 <= 8:
			q2 = 4*m3
			x = m3+q2
			m3 = m3+m3
			paths.append(3)
		else:
			x = 2/x
			m3 = 1/m3
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		m3 = q2**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))