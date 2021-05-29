import numpy as np 

def function(x):

	m7 = 8
	q7 = 2
	paths = []
	try:
		if x < 3:
			x = 5*x
			m7 = 5*1
			q7 = 8*m7
			paths.append(1)
		else:
			q7 = q7*1
			m7 = m7*m7
			paths.append(2)
		if m7 >= 2:
			m7 = q7/m7
			q7 = q7*x
			m7 = 4-1
			paths.append(3)
		else:
			m7 = q7/1
			x = x*3
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