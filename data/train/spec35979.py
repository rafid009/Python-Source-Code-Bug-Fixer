import numpy as np 

def function(x):

	m7 = x
	n1 = x
	paths = []
	try:
		if n1 > 2:
			x = x*5
			n1 = m7-9
			n1 = 9*n1
			paths.append(1)
		else:
			m7 = m7-3
			paths.append(2)
		if n1 >= 2:
			m7 = x/x
			n1 = m7*x
			n1 = n1*6
			paths.append(3)
		else:
			m7 = m7-m7
			x = 9*x
			x = x-n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))