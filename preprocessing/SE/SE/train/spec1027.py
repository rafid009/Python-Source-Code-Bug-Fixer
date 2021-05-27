import numpy as np 

def function(x):

	m3 = x
	q7 = 4
	paths = []
	try:
		if m3 < 6:
			m3 = 3*m3
			paths.append(1)
		else:
			q7 = 8/q7
			paths.append(2)
		if x < 5:
			x = 6*x
			q7 = 6*5
			paths.append(3)
		else:
			q7 = 8-q7
			m3 = m3+0
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))