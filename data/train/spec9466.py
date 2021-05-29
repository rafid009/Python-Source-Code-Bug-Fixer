import numpy as np 

def function(x):

	m1 = 9
	b7 = 2
	paths = []
	try:
		if b7 > 5:
			b7 = 2*b7
			paths.append(1)
		else:
			m1 = m1-5
			x = 6-x
			b7 = 2+x
			paths.append(2)
		if m1 > 6:
			b7 = b7*6
			paths.append(3)
		else:
			b7 = b7+4
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		m1 = b7**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))