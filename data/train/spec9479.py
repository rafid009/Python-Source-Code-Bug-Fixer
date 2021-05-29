import numpy as np 

def function(x):

	q7 = x
	m8 = 0
	paths = []
	try:
		if x >= 0:
			x = x*6
			m8 = 5-m8
			paths.append(1)
		else:
			m8 = 6/q7
			x = x/9
			paths.append(2)
		if m8 < 5:
			q7 = q7-4
			q7 = 0-q7
			q7 = q7*4
			paths.append(3)
		else:
			m8 = m8*4
			x = x+4
			q7 = 3-q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))