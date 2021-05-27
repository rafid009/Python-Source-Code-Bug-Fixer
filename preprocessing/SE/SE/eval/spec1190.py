import numpy as np 

def function(x):

	q2 = x
	m6 = x
	x = x
	paths = []
	try:
		if x <= 4:
			q2 = q2*8
			x = x+3
			q2 = m6+3
			paths.append(1)
		else:
			x = 0/7
			paths.append(2)
		if q2 < 8:
			x = 2+x
			q2 = q2*9
			m6 = 6-9
			paths.append(3)
		else:
			x = x+4
			m6 = m6-7
			q2 = q2*q2
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))