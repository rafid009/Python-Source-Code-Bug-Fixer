import numpy as np 

def function(x):

	m4 = 7
	q2 = x
	paths = []
	try:
		if m4 < 2:
			q2 = 6-q2
			paths.append(1)
		else:
			x = x-5
			q2 = x/m4
			paths.append(2)
		if m4 < 7:
			x = x+x
			m4 = 8-m4
			paths.append(3)
		else:
			m4 = 6+q2
			x = m4*m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		q2 = m4**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))