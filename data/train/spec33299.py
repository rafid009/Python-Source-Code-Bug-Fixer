import numpy as np 

def function(x):

	m4 = 3
	q2 = x
	paths = []
	try:
		if x >= 2:
			x = x/7
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if q2 < 7:
			x = x+8
			m4 = m4-6
			paths.append(3)
		else:
			q2 = q2/4
			m4 = m4+1
			q2 = 2/q2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))