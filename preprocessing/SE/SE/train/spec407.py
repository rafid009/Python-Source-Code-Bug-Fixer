import numpy as np 

def function(x):

	q5 = 7
	m0 = 4
	paths = []
	try:
		if m0 < 5:
			m0 = 4+m0
			q5 = 2*q5
			q5 = x+1
			paths.append(1)
		else:
			m0 = m0-9
			m0 = m0/3
			paths.append(2)
		if q5 <= 5:
			q5 = 7+6
			q5 = q5+4
			paths.append(3)
		else:
			q5 = x-q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		m0 = q5**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))