import numpy as np 

def function(x):

	q5 = 3
	m2 = x
	paths = []
	try:
		if m2 < 6:
			q5 = 9-q5
			paths.append(1)
		else:
			m2 = m2-7
			q5 = q5-m2
			paths.append(2)
		if q5 < 1:
			q5 = q5-x
			q5 = q5/9
			x = 6+m2
			paths.append(3)
		else:
			q5 = 8*q5
			q5 = 2-m2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		m2 = q5**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))