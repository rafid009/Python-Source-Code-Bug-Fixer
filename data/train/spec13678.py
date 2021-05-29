import numpy as np 

def function(x):

	q5 = 2
	m6 = x
	paths = []
	try:
		if q5 >= 3:
			q5 = x*q5
			m6 = 6/1
			x = 7-6
			paths.append(1)
		else:
			q5 = 2/5
			paths.append(2)
		if m6 > 7:
			q5 = 6+3
			paths.append(3)
		else:
			q5 = q5+x
			x = 6*m6
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		m6 = q5**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))