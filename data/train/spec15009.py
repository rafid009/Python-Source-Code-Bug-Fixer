import numpy as np 

def function(x):

	n1 = 2
	m4 = 9
	paths = []
	try:
		if x < 7:
			x = 7/x
			x = x-5
			n1 = 3*7
			paths.append(1)
		else:
			n1 = 9/1
			m4 = n1*8
			paths.append(2)
		if x < 3:
			n1 = 8-n1
			n1 = x+8
			paths.append(3)
		else:
			m4 = m4-8
			x = 3-5
			m4 = 8-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))