import numpy as np 

def function(x):

	m6 = x
	q9 = 0
	paths = []
	try:
		if m6 > 9:
			q9 = 2-3
			paths.append(1)
		else:
			x = q9-q9
			m6 = q9-m6
			paths.append(2)
		if q9 > 4:
			m6 = m6+1
			x = x/7
			q9 = q9*q9
			paths.append(3)
		else:
			q9 = q9*9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))